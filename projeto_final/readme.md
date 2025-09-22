# Agente de IA para Geração de Testes Unitários com Pytest

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Testing-lightgrey.svg)

---

### Tabela de Conteúdos
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Como Executar](#como-executar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Estrutura do Repositório](#estrutura-do-repositório)

---

## Visão Geral do Projeto

Este projeto consiste na criação de um agente de Inteligência Artificial capaz de automatizar a escrita de testes unitários para código Python. A aplicação utiliza o poder dos Grandes Modelos de Linguagem (LLMs) através do serviço **Azure OpenAI**, orquestrado pela biblioteca **LangChain**, para analisar funções Python e gerar testes robustos no formato da biblioteca **`pytest`**.

O objetivo é resolver o desafio comum e muitas vezes demorado da criação de testes, aumentando a produtividade do desenvolvedor e incentivando a adoção de boas práticas de qualidade de software. Este trabalho foi desenvolvido como parte de um desafio de projeto da [DIO](https://www.dio.me/).

## Funcionalidades

-   **Análise de Código:** O agente lê e interpreta o conteúdo de um arquivo Python fornecido.
-   **Geração Automática de Testes:** Cria um arquivo de teste (`test_*.py`) correspondente ao código analisado.
-   **Cobertura Abrangente:** Gera casos de teste para cenários de sucesso ("caminho feliz") e cenários de falha e de borda (*edge cases*).
-   **Validação de Exceções:** Utiliza `pytest.raises` para garantir que as funções levantam as exceções esperadas em casos de erro (ex: divisão por zero).

## Tecnologias Utilizadas

-   **Linguagem:** Python 3.9+
-   **IA & Orquestração:**
    -   `LangChain`: Framework para desenvolver aplicações com LLMs, utilizado para criar o prompt e a cadeia de execução.
    -   `Azure OpenAI`: Serviço de nuvem da Microsoft que fornece acesso a modelos de linguagem avançados (GPT-3.5-Turbo, GPT-4, etc.).
-   **Biblioteca de Testes:**
    -   `pytest`: Framework para a escrita e execução dos testes gerados.
-   **Gerenciamento de Dependências:**
    -   `pip` e `requirements.txt`
-   **Gerenciamento de Segredos:**
    -   `python-dotenv`: Para carregar as credenciais da API de forma segura a partir de um arquivo `.env`.

## Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

#### 1. Pré-requisitos
-   Python 3.9 ou superior instalado.
-   Git instalado.
-   Uma conta no **Microsoft Azure** com acesso ao serviço **Azure OpenAI** e um modelo de texto (como `gpt-35-turbo`) já implantado.

#### 2. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/pytest_agent.git](https://github.com/seu-usuario/pytest_agent.git)
cd pytest_agent
