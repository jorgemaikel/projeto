import os
import base64
from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import AzureOpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- 1. CONFIGURAÇÃO DO CLIENTE AZURE OPENAI ---
# Pega as credenciais do ambiente
api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = "2024-02-01" # Versão da API

# Inicializa o cliente do Azure OpenAI
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=api_endpoint
)

# --- 2. PROMPT ENGINEERING: O "CÉREBRO" DA ANÁLISE ---
# Este prompt detalhado ensina a IA a fazer a análise STRIDE
PROMPT_STRIDE = """
Você é um especialista em cibersegurança e modelagem de ameaças. Sua tarefa é analisar o diagrama de arquitetura de aplicação fornecido e gerar uma análise de ameaças detalhada baseada na metodologia STRIDE.

A metodologia STRIDE classifica as ameaças em 6 categorias:

1.  **Spoofing (Falsificação de Identidade):** Ameaças que envolvem um ator malicioso se passando por outra entidade.
    * Exemplos: Usar credenciais roubadas, falsificar endereços de e-mail, enganar um sistema para que pense que é outro.
    * *Pergunta a se fazer:* Quem pode se passar por um usuário, serviço ou componente legítimo?

2.  **Tampering (Violação/Adulteração de Dados):** Ameaças que envolvem a modificação não autorizada de dados, seja em trânsito ou em repouso.
    * Exemplos: Alterar dados em um banco de dados, modificar uma mensagem em trânsito.
    * *Pergunta a se fazer:* Onde os dados podem ser modificados sem autorização?

3.  **Repudiation (Repúdio):** Ameaças que permitem que um ator negue ter realizado uma ação, pois não há provas suficientes.
    * Exemplos: Um sistema que não gera logs de auditoria para ações críticas.
    * *Pergunta a se fazer:* Como um usuário poderia negar ter feito uma operação? Faltam logs?

4.  **Information Disclosure (Divulgação de Informações):** Ameaças que envolvem a exposição de informações sensíveis a indivíduos não autorizados.
    * Exemplos: Vazamento de dados pessoais, exposição de senhas, acesso a arquivos confidenciais.
    * *Pergunta a se fazer:* Onde informações sensíveis podem ser expostas?

5.  **Denial of Service (Negação de Serviço - DoS):** Ameaças que visam tornar um sistema ou recurso indisponível para seus usuários legítimos.
    * Exemplos: Inundar um servidor com requisições, consumir todos os recursos de um serviço.
    * *Pergunta a se fazer:* Como um atacante poderia travar ou tornar este sistema indisponível?

6.  **Elevation of Privilege (Elevação de Privilégio):** Ameaças que permitem que um usuário com privilégios limitados ganhe acesso a funções de um usuário com privilégios mais altos.
    * Exemplos: Um usuário comum conseguindo acesso de administrador.
    * *Pergunta a se fazer:* Como um usuário com poucos privilégios poderia ganhar mais acesso do que deveria?

**Sua Tarefa:**
Analise a imagem do diagrama de arquitetura anexa. Para cada componente (ex: Frontend, API, Banco de Dados) e cada fluxo de dados (as setas), identifique potenciais ameaças para cada uma das 6 categorias STRIDE. Apresente sua análise em formato Markdown, organizada por categoria. Seja específico e justifique suas conclusões com base no diagrama.
"""

# --- 3. INICIALIZAÇÃO DA API FASTAPI ---
app = FastAPI(
    title="API de Análise de Ameaças STRIDE",
    description="Faça o upload de um diagrama de arquitetura para receber uma análise de ameaças automatizada usando Azure OpenAI e a metodologia STRIDE."
)

# --- 4. LÓGICA DA API ---
async def analisar_imagem_stride(image_bytes: bytes):
    """
    Converte a imagem para base64 e envia para o Azure OpenAI com o prompt STRIDE.
    """
    # Converte os bytes da imagem para uma string base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    try:
        response = client.chat.completions.create(
            model=api_deployment,
            messages=[
                { "role": "system", "content": "Você é um especialista em cibersegurança." },
                { "role": "user", "content": [
                    {
                        "type": "text",
                        "text": PROMPT_STRIDE
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]}
            ],
            max_tokens=2048 # Aumente se as análises estiverem sendo cortadas
        )
        return response.choices[0].message.content

    except Exception as e:
        # Lida com possíveis erros da API
        raise HTTPException(status_code=500, detail=f"Erro ao contatar a API da OpenAI: {str(e)}")


@app.post("/analisar-ameacas/", summary="Analisa um diagrama de arquitetura")
async def analisar_ameacas_endpoint(file: UploadFile = File(..., description="Imagem do diagrama de arquitetura (PNG, JPG, etc.)")):
    """
    Recebe uma imagem de um diagrama, envia para a análise STRIDE via Azure OpenAI
    e retorna o relatório de ameaças.
    """
    # Lê os bytes do arquivo enviado
    image_bytes = await file.read()

    # Chama a função principal de análise
    threat_analysis_report = await analisar_imagem_stride(image_bytes)

    return {
        "file_name": file.filename,
        "threat_analysis": threat_analysis_report
    }

# --- 5. ROTA RAIZ PARA TESTE ---
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Análise de Ameaças STRIDE. Vá para /docs para testar."}
