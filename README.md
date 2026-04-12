#  LangGraph Chatbot

A conversational AI chatbot built with **LangGraph** for stateful graph-based dialogue management, powered by a local **Ollama** LLM and served through an interactive **Streamlit** UI.

---

##  Overview

This project demonstrates how to build a stateful chatbot using LangGraph's `StateGraph`. The graph manages the flow of conversation — passing state between nodes on each turn — while Ollama runs the language model locally (no API keys required). Streamlit provides a clean, browser-based chat interface.

---

##  Tech Stack

| Layer | Tool |
|---|---|
| Graph / Agent Framework | [LangGraph](https://github.com/langchain-ai/langgraph) |
| LLM Backend | [Ollama](https://ollama.com/) (local) |
| UI | [Streamlit](https://streamlit.io/) |
| Language | Python 3.10+ |

---

##  Project Structure

```
Langraph-Chatbot/
└── Chatbot/
    ├── frontend.py        
    └── backend.py            
```

---

##  Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com/download) installed and running locally
- A model pulled via Ollama 

Pull a model before running:
```bash
ollama pull llama3.2:1b
```

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/VinitAgarwal21/Langraph-Chatbot.git
cd Langraph-Chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If there is no `requirements.txt`, install the core packages manually:
> ```bash
> pip install langgraph langchain-community streamlit ollama
> ```

### 4. Start the Ollama server

Make sure Ollama is running in the background:
```bash
ollama serve
```

### 5. Run the Streamlit app

```bash
cd Chatbot
streamlit run app.py
```

Open your browser at **http://localhost:8501** to start chatting.

---

##  How It Works

1. **State Management** — LangGraph's `StateGraph` holds the conversation history as a typed state dict that is passed between nodes on every turn.
2. **Chatbot Node** — A single `chatbot` node calls the Ollama-backed LLM with the current message history and appends the response back to state.
3. **Graph Compilation** — Edges connect `START → chatbot → END`, forming a simple but extensible loop.
4. **Streamlit UI** — User inputs are fed into the graph via `graph.stream(...)`, and responses are displayed in a chat-style interface.

```
User Input
    │
    ▼
┌─────────────┐
│  StateGraph  │
│             │
│  [chatbot]  │  ◄── Ollama LLM
│             │
└─────────────┘
    │
    ▼
 Response
```

---

## 🔧 Configuration

To switch the Ollama model, update the model name in `chatbot.py`:

```python
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2:1b")   # Change to any model you have pulled
```

---

##  Dependencies

- `langgraph` — Graph-based agent/workflow framework
- `langchain-community` — Ollama LLM integration
- `streamlit` — Web UI
- `ollama` — Local model runner

---

##  Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License

This project is open source. Feel free to use and modify it.

---

> Built with ❤️ using LangGraph + Ollama + Streamlit
