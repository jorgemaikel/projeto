# Projeto: Análise de Ameaças STRIDE Automatizada com IA

Este projeto implementa uma API em Python utilizando FastAPI e o serviço Azure OpenAI para realizar uma análise de modelagem de ameaças baseada na metodologia STRIDE a partir de um diagrama de arquitetura.

## Descrição

A aplicação recebe uma imagem de um diagrama de arquitetura, utiliza um modelo de visão do Azure OpenAI (GPT-4o) e, através de técnicas de Prompt Engineering, gera um relatório de potenciais ameaças de cibersegurança, classificadas de acordo com as 6 categorias do STRIDE:
-   **S**poofing (Falsificação)
-   **T**ampering (Violação)
-   **R**epudiation (Repúdio)
-   **I**nformation Disclosure (Divulgação de Informações)
-   **D**enial of Service (Negação de Serviço)
-   **E**levation of Privilege (Elevação de Privilégio)

## Tech Stack

-   **Linguagem:** Python 3.9+
-   **API Framework:** FastAPI
-   **Servidor:** Uvicorn
-   **IA Generativa:** Azure OpenAI (GPT-4o / GPT-4 Turbo with Vision)
-   **Bibliotecas:** `openai`, `python-dotenv`, `python-multipart`

## Configuração do Ambiente

1.  **Pré-requisitos:**
    * Conta no Microsoft Azure
    * Recurso do Azure OpenAI com um modelo de visão implantado (ex: `gpt-4o`)

2.  **Instalação Local:**
    * Clone este repositório: `git clone <URL_DO_SEU_REPOSITORIO>`
    * Crie e ative um ambiente virtual:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    * Instale as dependências:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Variáveis de Ambiente:**
    * Crie um arquivo `.env` na raiz do projeto e preencha com suas credenciais do Azure OpenAI:
        ```
        AZURE_OPENAI_ENDPOINT="SEU_ENDPOINT"
        AZURE_OPENAI_API_KEY="SUA_CHAVE"
        AZURE_OPENAI_DEPLOYMENT_NAME="NOME_DA_SUA_IMPLANTAÇÃO"
        ```

## Como Executar

1.  Inicie o servidor FastAPI com o Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
2.  Acesse a documentação interativa da API em seu navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
3.  Utilize a interface para fazer o upload de um diagrama de arquitetura e receber a análise de ameaças.

## Exemplo de Resposta

(Opcional: Coloque aqui uma captura de tela da resposta da API ou um exemplo de texto)

```json
{
  "file_name": "arquitetura_web.png",
  "threat_analysis": "## Análise de Ameaças STRIDE\n\n### Spoofing (Falsificação de Identidade)\n- **Ameaça:** Um usuário mal-intencionado pode tentar se passar por um usuário legítimo no Frontend para obter acesso não autorizado à API.\n- **Mitigação:** Implementar autenticação forte (MFA).\n\n### Tampering (Violação de Dados)\n- **Ameaça:** Os dados em trânsito entre a API e o Banco de Dados podem ser interceptados e modificados se a conexão não for criptografada.\n- **Mitigação:** Utilizar TLS para todas as comunicações internas.\n\n[... continuação da análise ...]"
}
