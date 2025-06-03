# 🧠 Retrieval-Augmented Generation (RAG) System with Local Vector Store

This project implements a complete Retrieval-Augmented Generation (RAG) pipeline using open-source tools and integrates with large language models (LLMs) from **NGU** and **GROQ** via custom API endpoints. The system loads local documents, processes them into chunks, embeds them using sentence-transformers, stores them using FAISS, and retrieves the most relevant content to augment language generation.

---

## 📦 Features

- 🔍 Loads and processes local `.pdf`, `.txt`, and `.docx` documents
- ✂️ Chunks documents with overlap handling
- 🧠 Embeds text using HuggingFace transformers
- 💾 Stores embeddings in FAISS for fast retrieval
- 🤖 Integrates with GROQ or NGU LLMs via `.env` config
- 🧵 Custom RAG pipeline using prompt injection into chat completion API

---

## 📁 Folder Structure
rag_project/
├── documents/ # Your source documents (PDF, TXT, DOCX)
├── rag_code/
│ ├── load_documents.py # Loads files from disk
│ ├── split_documents.py # Chunks text with overlap
│ ├── vector_store.py # Embeds and saves to FAISS
│ ├── rag_pipeline.py # Custom retriever + LLM integration
├── main.py # Entry point for running RAG query
├── .env # API keys and model configs
├── README.md # This file
├── requirements.txt # All dependencies

yaml
Copy
Edit

---

## 🧪 Setup Instructions

### 1. Clone & Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt


# NGU
NGU_API_KEY="#########"
NGU_BASE_URL="https://ngullama.femtoid.com/v1"
NGU_MODEL="qwen2.5-coder:7b"

# GROQ
GROQ_API_KEY="your-groq-api-key-here"
GROQ_BASE_URL="https://api.groq.com/openai/v1"
GROQ_MODEL="llama-3.3-70b-versatile"

# Select which provider to use
MODEL_SERVER="NGU"


 Run the System
bash
Copy
Edit
python main.py



"What is retrieval-augmented generation?"

