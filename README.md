# 🎵 Atendimento Inteligente - Empório da Música

Protótipo de agente conversacional de atendimento ao cliente desenvolvido para a loja **Empório da Música**. O sistema integra de forma híbrida **dados tabulares (CSV)** via *Function Calling* e **documentos de políticas (PDF)** utilizando a API oficial do Google Gemini, tudo encapsulado em uma interface gráfica interativa desenvolvida em **Streamlit**.

---

## 💡 Sobre o Projeto e Arquitetura

Este projeto foi desenvolvido com foco em agilidade, robustez e simplicidade para atender a um escopo de entrega rápida (Sprint de 12 horas). 

### Por que escolhemos esta Stack?
* **Google Gemini API:** Utilizado pelo seu suporte nativo e eficiente a *Function Calling*, além de uma ampla janela de contexto que permite injetar regras de negócio diretamente nas instruções de sistema.
* **Pandas e PyPDF2:** Optamos por carregar o catálogo de produtos (`products.csv`) diretamente em memória utilizando o **Pandas** e as políticas institucionais (`políticas_da_loja.pdf`) via **PyPDF2**, eliminando a necessidade de configurar bancos de dados externos pesados e mantendo a latência extremamente baixa.
* **Streamlit:** Permite construir uma interface de chat completa em Python puro, dispensando a complexidade de rotas, configuração de CORS e gerenciamento de estado de um front-end em React.

---

## ⚙️ Configurações para Levantar o Projeto

### 1. Clonar o Repositório e Configurar o Ambiente Virtual (venv)
Abra o seu terminal na pasta do projeto e crie um ambiente virtual isolado para gerenciar as dependências do Python:

```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows (PowerShell): .venv\Scripts\activate
```

### 2. Instalação das Dependências
Para garantir que o SDK moderno do Google GenAI, o Streamlit, o Pandas e o leitor de PDF estejam disponíveis, execute os comandos de instalação:

```bash
pip install -U google-genai
pip install streamlit pypdf2 pandas
```

*(Opcional - Desenvolvimento CLI)*: Se desejar instalar as ferramentas de suporte do Google AI Studio para o seu terminal, você pode executar o script de instalação oficial:
```bash
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
export PATH="$PATH:$HOME/.local/bin"
```

---

## 🔑 Configuração do Google AI Studio e Chave de API

Para que o agente consiga se comunicar com os modelos de IA, você precisará de uma chave de acesso oficial:

1. Acesse o [Google AI Studio](https://aistudio.google.com/) e faça login com sua conta do Google.
2. No painel principal, clique em **"Get API key"** (ou vá até a seção de chaves) para gerar uma nova credencial gratuita. Ela será gerada no formato padrão iniciando com o prefixo `AIza...`.
3. **Segurança de Credenciais:** Nunca cole sua chave de API diretamente no código-fonte. Armazene-a de forma segura como uma variável de ambiente no seu terminal antes de executar o projeto:

* **No Linux / macOS:**
  ```bash
  export GEMINI_API_KEY="sua_chave_aqui_comecando_com_aiza"
  ```
* **No Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="sua_chave_aqui_comecando_com_aiza"
  ```

No código da aplicação (`app.py`), o cliente da API busca essa variável de ambiente de forma segura utilizando o seguinte trecho:
```python
import os
from google import genai

# Inicializa o cliente buscando a chave do ambiente
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```

Posteriormente, o modelo selecionado (como o `gemini-3.1-flash-lite`) é configurado juntamente com as ferramentas de *Function Calling* e as instruções de sistema:
```python
st.session_state.chat_session = client.chats.create(
    model="gemini-3.1-flash-lite", 
    config=types.GenerateContentConfig(
        system_instruction=instrucoes,
        tools=[consultar_produto],
        temperature=0.3
    )
)
```

---

## 🚀 Executando a Interface Gráfica

Com o ambiente virtual ativado, as dependências instaladas e a variável de ambiente `GEMINI_API_KEY` devidamente configurada no seu terminal, inicie a aplicação através do Streamlit:

```bash
streamlit run app.py
```

O Streamlit irá compilar o script e abrir automaticamente uma aba no seu navegador web padrão no endereço local: **`http://localhost:8501`**.

---

## 📝 Próximos Passos (Evolução com Mais Tempo)
* Integração completa das tabelas relacionais restantes (`customers.csv`, `orders.csv`, `order_items.csv`) para análise de perfil e histórico de compras dos clientes.
* Implementação de banco de dados vetorial (como ChromaDB) para indexação escalável de bases documentais extensas.