import os
from dotenv import load_dotenv
import requests
from langchain.chains import RetrievalQA

load_dotenv()

# Read model configuration
MODEL_SERVER = os.getenv('MODEL_SERVER', 'GROQ').upper()
if MODEL_SERVER == "GROQ":
    API_KEY = os.getenv('GROQ_API_KEY')
    BASE_URL = os.getenv('GROQ_BASE_URL')
    MODEL_NAME = os.getenv('GROQ_MODEL')
elif MODEL_SERVER == "NGU":
    API_KEY = os.getenv('NGU_API_KEY')
    BASE_URL = os.getenv('NGU_BASE_URL')
    MODEL_NAME = os.getenv('NGU_MODEL')
else:
    raise ValueError(f"Unsupported MODEL_SERVER: {MODEL_SERVER}")

# Manual chat completion wrapper
def chat_completion(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")
    return response.json()['choices'][0]['message']['content']


# Build a basic RAG pipeline without langchain's LLM
def build_rag_chain(vector_db):
    retriever = vector_db.as_retriever()
    return retriever


def query_rag(retriever, question):
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs[:4]])  # limit to top 4
    prompt = f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}"
    return chat_completion(prompt)
