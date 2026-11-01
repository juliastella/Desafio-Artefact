import streamlit as st
from google import genai
from google.genai import types
from src.data_loader import produtos_df, texto_politicas

st.set_page_config(page_title="Empório da Música")
st.title("🎵 Atendimento - Empório da Música")

# Inicializa o cliente da API
# Inicializa o cliente da API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Ferramenta para o modelo (Function Calling)
def consultar_produto(nome_produto: str) -> str:
    """Consulta preço e estoque de um produto no banco de dados da loja."""
    resultado = produtos_df[produtos_df["product_name"].str.contains(nome_produto, case=False, na=False)]
    if resultado.empty:
        return f"Produto '{nome_produto}' não encontrado."
    item = resultado.iloc[0]
    return f"Produto: {item['product_name']} | Preço: R${item['price']} | Estoque: {item['stock']}"

# Inicializa a sessão de chat injetando a persona, PDF e as ferramentas
if "chat_session" not in st.session_state:
    instrucoes = f"""Você é o agente de atendimento da loja Empório da Música.
Regras da loja (trocas, prazos, etc): {texto_politicas}
Para responder sobre valores ou disponibilidade, utilize sempre a ferramenta consultar_produto."""

    st.session_state.chat_session = client.chats.create(
        model="gemini-3.1-flash-lite", 
        config=types.GenerateContentConfig(
            system_instruction=instrucoes,
            tools=[consultar_produto],
            temperature=0.3
        )
    )
    st.session_state.messages = []

# Renderiza o histórico na tela
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["text"])

# Captura e envia a nova mensagem
pergunta = st.chat_input("Como posso ajudar hoje?")
if pergunta:
    st.chat_message("user").write(pergunta)
    st.session_state.messages.append({"role": "user", "text": pergunta})
    
    # Chama o modelo no modo streaming e cria um gerador de texto
    resposta_stream = st.session_state.chat_session.send_message_stream(pergunta)
    
    # O Streamlit renderiza as palavras em tempo real e captura o texto final
    with st.chat_message("assistant"):
        texto_final = st.write_stream((chunk.text for chunk in resposta_stream))
        
    st.session_state.messages.append({"role": "assistant", "text": texto_final})
