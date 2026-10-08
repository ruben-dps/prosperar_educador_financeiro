# 💰 Agente Prosperar - Educador Financeiro Pessoal

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![LLM Runtime](https://img.shields.io/badge/Ollama-gpt--oss-black.svg)](https://ollama.ai/)

O **Prosperar** é um assistente virtual interativo e inteligente focado **exclusivamente em Educação Financeira Pessoal**. Ele combina modelos de linguagem (LLMs via Ollama) com a análise de dados financeiros do usuário para transformar conceitos complexos do mercado financeiro em lições simples, didáticas e personalizadas.

---

## 📌 Sumário
- [Visão Geral e Objetivos](#-visão-geral-e-objetivos)
- [Principais Funcionalidades](#-principais-funcionalidades)
- [Arquitetura e Estrutura do Projeto](#-arquitetura-e-estrutura-do-projeto)
- [Regras Rígidas do Agente (System Prompt)](#-regras-rígidas-do-agente-system-prompt)
- [Base de Conhecimento e Dados](#-base-de-conhecimento-e-dados)
- [Pré-requisitos e Instalação](#-pré-requisitos-e-instalação)
- [Como Executar a Aplicação](#-como-executar-a-aplicação)
- [Avaliação de Desempenho e Métricas](#-avaliação-de-desempenho-e-métricas)
- [Pitch do Projeto](#-pitch-do-projeto)

---

## 🎯 Visão Geral e Objetivos

Diferente de assistentes de instituições financeiras que buscam vender produtos, o **Prosperar** atua como um **tutor neutro e amigável**. Ele analisa o perfil cadastral, a renda, os gastos mensais e as metas do cliente para explicar termos como *Selic, CDI, LCI/LCA, inflação e reserva de emergência* através da própria realidade do usuário.

### Para quem serve?
* Pessoas que buscam organizar o orçamento familiar.
* Iniciantes que desejam entender onde colocar o dinheiro sem sofrer com termos técnicos (*juridiquês/economês*).
* Usuários que buscam uma ferramenta interativa e privada para tirar dúvidas de finanças pessoais sem viés comercial.

---

## ✨ Principais Funcionalidades

1. **Exemplificação Personalizada**: Utiliza os dados reais de renda, metas e histórico de transações do cliente para ilustrar cada conceito.
2. **Interface Amigável em Streamlit**: Chat em tempo real com painel lateral apresentando o resumo financeiro do usuário.
3. **Privacidade Garantida**: Processamento de IA 100% local através do Ollama (`gpt-oss`), sem envio de dados pessoais para APIs de terceiros.
4. **Recusa Ativa de Desvios de Escopo**: O agente foca 100% em finanças e recusa perguntas que não pertencem ao tema.
5. **Garantia de Neutralidade**: Proibido de recomendar investimentos específicos ou indicar alocação de capital.

---

## 🏗️ Arquitetura e Estrutura do Projeto

O projeto adota uma estrutura modular de diretórios, separando os scripts de código-fonte (`src/`) das bases de dados locais (`data/`):

```text
prosperar-educador-financeiro/
├── data/
│   ├── perfil_investidor.json      # Dados cadastrais, renda, reserva atual e metas
│   ├── produtos_financeiros.json   # Catálogo educativo de produtos de renda fixa e variável
│   ├── transacoes.csv              # Extrato mensal de receitas e despesas
│   └── historico_atendimento.csv   # Histórico das últimas interações do cliente
├── src/
│   └── app.py                      # Aplicação principal Streamlit e integração Ollama
├── .gitignore
├── requirements.txt                # Dependências Python do projeto
└── README.md                       # Documentação completa
