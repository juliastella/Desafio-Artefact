import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Empório da Música")
st.title("🎵 Atendimento - Empório da Música")

client = genai.Client()

# Inicializa a sessão de chat e a persona do modelo
if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-1.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Você é o agente de atendimento da loja Empório da Música. Responda de forma educada e baseada estritamente nos dados da loja."
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
    
    resposta = st.session_state.chat_session.send_message(pergunta)
    
    st.chat_message("assistant").write(resposta.text)
    st.session_state.messages.append({"role": "assistant", "text": resposta.text})