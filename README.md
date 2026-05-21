# Agentic AI Chatbot

An intelligent Agentic RAG Chatbot built using LangGraph, Streamlit, FAISS, and LLMs.

This chatbot can:

* Answer questions from uploaded PDFs
* Search the web dynamically
* Use routing logic to decide between PDF or Web Search
* Evaluate responses using DeepEval
* Provide an interactive chat interface using Streamlit

---

# Features

## PDF Question Answering

Upload PDF files and ask questions from documents.

## Web Search Support

If information is not present in PDF, the agent can search the web.

## Agentic Routing

Uses conditional routing logic to decide:

* PDF Retrieval
* Web Search

## Vector Database

Uses FAISS for semantic similarity search.

## LLM Integration

Supports:

* Groq
* Gemini
* OpenAI

## DeepEval Metrics

Evaluates:

* Faithfulness
* Answer Relevancy

## Streamlit UI

Simple and interactive web interface.

---

# Tech Stack

* Python
* Streamlit
* LangChain
* LangGraph
* FAISS
* HuggingFace Embeddings
* DeepEval
* Groq API
* Gemini API

---

# Project Structure

```bash
Agentic-AI-Chatbot/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── rag/
│   ├── graph.py
│   ├── evaluator.py
│   ├── retriever.py
│   ├── llm.py
│   └── prompts.py
│
├── data/
│   └── sample.pdf
│
└── vectorstore/
```

---

# Workflow

```text
User Question
      │
      ▼
Router Decision
 ┌───────────────┐
 │ use_web=True  │──► Web Search
 └───────────────┘
 │
 ▼
PDF Retrieval
 │
 ▼
LLM Generation
 │
 ▼
DeepEval Metrics
 │
 ▼
Final Response
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/aditya2129939/Agentic-AI-Chatbot.git
```

---

## 2. Move into Project Folder

```bash
cd Agentic-AI-Chatbot
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

---

# Run the Project

```bash
streamlit run main.py
```

---

# Example Questions

* What is machine learning?
* Explain neural networks from the PDF.
* Search latest AI news.
* What is if else statement?

---

# Future Improvements

* Memory support
* Multi-PDF upload
* Voice assistant
* Chat history
* Hybrid search
* Deployment on cloud

---

# Author

Aditya Vishwakarma

---

# License

This project is for educational and learning purposes.
