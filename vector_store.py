from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def build_vector_store(chunks, model_name="all-MiniLM-L6-v2", path="faiss_index"):
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    db = FAISS.from_documents(chunks, embedder)
    db.save_local(path)
    return db

def load_vector_store(model_name="all-MiniLM-L6-v2", path="faiss_index"):
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    return FAISS.load_local(path, embedder)
