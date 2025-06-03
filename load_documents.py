import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

def load_documents(folder_path='documents'):
    docs = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        try:
            if filename.endswith(".pdf"):
                docs.extend(PyPDFLoader(path).load())
            elif filename.endswith(".txt"):
                docs.extend(TextLoader(path).load())
            elif filename.endswith(".docx"):
                docs.extend(Docx2txtLoader(path).load())
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    return docs
