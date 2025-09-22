import os
import re
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain.schema.output_parser import StrOutputParser


CODE_TO_TEST = """
def soma(a: float, b: float) -> float:
    \"\"\"
    Esta função retorna a soma de dois números.
    \"\"\"
    return a + b

def divisao(a: float, b: float) -> float:
    \"\"\"
    Esta função retorna a divisão de a por b.
    Levanta uma exceção ValueError se b for zero.
    \"\"\"
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def is_palindrome(text: str) -> bool:
    \"\"\"
    Verifica se um texto é um palíndromo.
    Ignora espaços e diferenças entre maiúsculas e minúsculas.
    \"\"\"
    if not isinstance(text, str):
        raise TypeError("A entrada deve ser uma string.")
    
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    return cleaned_text == cleaned_text[::-1]
"""



def configure_ai_client():
    """Carrega as variáveis de ambiente e configura o cliente do Azure OpenAI."""
    load_dotenv()
    
    try:
        model = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            api_version="2024-02-01"
        )
        return model
    except Exception as e:
        print(f"Erro ao configurar o cliente da Azure OpenAI: {e}")
        print("Verifique se as variáveis de ambiente estão definidas corretamente no arquivo .env")
        return None

def get_prompt_template():
    """Cria e retorna o template do prompt para a geração de testes."""
    return ChatPromptTemplate.from_template("""
Você é um Engenheiro de Qualidade de Software (QA) sênior, especialista em Python e na biblioteca pytest.
Sua tarefa é gerar testes unitários completos e de alta qualidade para o código Python fornecido.
