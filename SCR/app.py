import json
import os
import pandas as pd
import streamlit as st
from ollama import chat

# Configuração visual do Streamlit
st.set_page_config(
    page_title="Prosperar - Educador Financeiro",
    page_icon="💰",
    layout="centered"
)

# Caminhos absolutos para localizar a pasta data/ a partir de src/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "data"))

@st.cache_data
def carregar_dados():
    """Carrega os arquivos de dados da pasta data/."""
    perfil_path = os.path.join(DATA_DIR, 'perfil_investidor.json')
    produtos_path = os.path.join(DATA_DIR, 'produtos_financeiros.json')
    transacoes_path = os.path.join(DATA_DIR, 'transacoes.csv')
    historico_path = os.path.join(DATA_DIR, 'historico_atendimento.csv')

    with open(perfil_path, 'r', encoding='utf-8') as f:
        perfil = json.load(f)

    with open(produtos_path, 'r', encoding='utf-8') as f:
        produtos = json.load(f)

    df_transacoes = pd.read_csv(transacoes_path)
    df_historico = pd.read_csv(historico_path) if os.path.exists(historico_path) else None

    return perfil, produtos, df_transacoes, df_historico

def construir_system_prompt(perfil, produtos, df_transacoes):
    """Monta o System Prompt injetando o contexto do cliente."""
    return f"""
Você é o Prosperar, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

DADOS DO CLIENTE (USAR COMO EXEMPLO CONTEXTUAL):
- Perfil e Metas: {json.dumps(perfil, ensure_ascii=False)}
- Opções Financeiras do Mercado: {json.dumps(produtos, ensure_ascii=False)}
- Amostra de Transações Recentes: {df_transacoes.head(5).to_dict(orient='records')}

REGRAS RÍGIDAS DE COMPORTAMENTO:
1. NUNCA recomende investimentos específicos (ex: "invista no produto X"). Apenas explique didaticamente como funcionam.
2. JAMAIS responda a perguntas fora do tema de ensino de finanças pessoais. Quando ocorrer, responda lembrando o seu papel de educador financeiro.
3. Use os dados fornecidos para dar exemplos personalizados (mencione valores da renda, despesas ou metas do cliente).
4. Use linguagem simples, leve e coloquial, como se estivesse conversando com um amigo.
5. Se não souber algo ou não possuir a informação solicitada, admita abertamente: "Não tenho essa informação, mas posso explicar..."
6. Sempre pergunte se o cliente entendeu no final da mensagem.
7. Responda de forma sucinta e direta, com NO MÁXIMO 3 parágrafos.
"""

st.title("💰 Agente Prosperar")
st.caption("Seu educador financeiro amigável e didático")

# Carregamento de Dados
try:
    perfil, produtos, df_transacoes, df_historico = carregar_dados()
    system_prompt = construir_system_prompt(perfil, produtos, df_transacoes)
except Exception as e:
    st.error(f"Erro ao carregar os arquivos na pasta 'data/': {e}")
    st.stop()

# Painel Lateral (Sidebar) com resumo do cliente
st.sidebar.header("📋 Perfil do Cliente")
st.sidebar.write(f"**Nome:** {perfil.get('nome', 'N/A')}")
st.sidebar.write(f"**Renda Mensal:** R$ {perfil.get('renda_mensal', 0):,.2f}")
st.sidebar.write(f"**Perfil:** {perfil.get('perfil_investidor', 'N/A').capitalize()}")
st.sidebar.write(f"**Reserva Atual:** R$ {perfil.get('reserva_emergencia_atual', 0):,.2f}")

st.sidebar.divider()
st.sidebar.subheader("🎯 Metas")
for m in perfil.get("metas", []):
    st.sidebar.write(f"- **{m['meta']}**: R$ {m['valor_necessario']:,.2f} (Até {m['prazo']})")

modelo = "gpt-oss"

# Inicialização do Histórico no Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Renderização das mensagens existentes
for msg in st.session_state.messages:
    if msg["role"] != "system":
        avatar = "🤖" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

# Caixa de Entrada do Usuário
if prompt := st.chat_input("Pergunte algo sobre finanças pessoais..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Pensando..."):
            try:
                response = chat(
                    model=modelo,
                    messages=st.session_state.messages
                )
                resposta_texto = response['message']['content']
                st.markdown(resposta_texto)
                st.session_state.messages.append({"role": "assistant", "content": resposta_texto})
            except Exception as e:
                st.error(f"Erro ao conectar ao Ollama (Modelo: {modelo}): {e}")
                st.info("Verifique se o Ollama está rodando (`ollama serve`) e se o modelo 'gpt-oss' foi baixado (`ollama pull gpt-oss`).")
