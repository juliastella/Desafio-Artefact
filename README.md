**Júlia Stella Silva de Paula - Full-Stack Developer | AI Software Engineer**

# 🎵 Intelligent Customer Support - Empório da Música

A conversational AI customer support prototype developed for **Empório da Música**. The system uses a hybrid architecture to integrate **tabular data (CSV)** through *Function Calling* and **policy documents (PDF)** using the official Google Gemini API. Everything is integrated into an interactive graphical interface built with **Streamlit**.

---

## 💡 Project Overview and Architecture

This project was developed with a focus on speed, reliability, and simplicity to meet a short delivery timeline (12-hour sprint).

### Why We Chose This Tech Stack

- **Google Gemini API:** Selected for its native and efficient support for *Function Calling*, as well as its large context window, which allows business rules to be injected directly into the system instructions.

- **Pandas and PyPDF2:** We chose to load the product catalog (`products.csv`) directly into memory using **Pandas** and extract the store policies from (`politicas_da_loja.pdf`) using **PyPDF2**. This eliminated the need to configure resource-intensive external databases while keeping response latency low.

- **Streamlit:** Allows us to build a fully functional chat interface using Python alone, avoiding the complexity of routing, CORS configuration, and state management typically associated with a React-based frontend.

---

## ⚙️ Project Setup

### 1. Clone the Repository and Set Up the Virtual Environment (venv)

Open your terminal in the project directory and create an isolated virtual environment to manage Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate

# On Windows (PowerShell):
# .venv\Scripts\activate
```

### 2. Install Dependencies

To ensure the Google GenAI SDK, Streamlit, Pandas, and PDF processing library are available, run the following installation commands:

```bash
pip install -U google-genai
pip install streamlit pypdf2 pandas
```

**(Optional - CLI Development):** If you want to install Google's AI Studio CLI support tools in your terminal, you can run the official installation script:

```bash
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
export PATH="$PATH:$HOME/.local/bin"
```

---

## 🔑 Google AI Studio Setup and API Key Configuration

To enable the agent to communicate with AI models, you will need an official API key:

1. Visit [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account.
2. On the main dashboard, click **"Get API key"** (or navigate to the API keys section) to generate a new free API key. It follows the standard format and typically starts with the `AIza...` prefix.
3. **Credential Security:** Never hardcode your API key directly into the source code. Store it securely as an environment variable in your terminal before running the application.

**Linux / macOS:**

```bash
export GEMINI_API_KEY="your_api_key_starting_with_aiza"
```

**Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY="your_api_key_starting_with_aiza"
```

In the application code (`app.py`), the API client securely retrieves this environment variable using the following code:

```python
import os
from google import genai

# Initialize the client using the environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```

Next, the selected model (such as `gemini-3.1-flash-lite`) is configured along with the *Function Calling* tools and system instructions:

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

## 🚀 Running the Application

Once the virtual environment is activated, dependencies are installed, and the `GEMINI_API_KEY` environment variable is properly configured in your terminal, start the application using Streamlit:

```bash
streamlit run app.py
```

Streamlit will execute the script and automatically open a new tab in your default web browser at the following local address:

**http://localhost:8501**

---

## 📝 Future Improvements (With Additional Development Time)

- Integrate the remaining relational datasets (`customers.csv`, `orders.csv`, and `order_items.csv`) to support customer profiling and purchase history analysis.
- Implement a vector database (such as ChromaDB) to enable scalable indexing and retrieval across larger document collections.

### 📚 Technical Documentation

For a detailed explanation of the project's architecture, technical decisions, and the rationale behind the technologies and implementation approaches, please refer to **[Architectural Decisions.pdf](Architectural%20Decisions.pdf)**, included in this repository.