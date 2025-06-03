from rag_code.load_documents import load_documents
from rag_code.split_documents import split_documents
from rag_code.vector_store import build_vector_store, load_vector_store
from rag_code.rag_pipeline import build_rag_chain, query_rag
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Step 1: Load and prepare documents
print("📄 Loading documents...")
docs = load_documents()

# Step 2: Split into chunks
print("✂️ Splitting documents...")
chunks = split_documents(docs)

if not chunks:
    print("❌ No chunks found. Please check your documents folder.")
    exit()

# Step 3: Create vector DB
print("🧠 Building vector store...")
vector_db = build_vector_store(chunks)

# Step 4: Set up RAG retrieval
print("🔗 Setting up RAG retriever...")
retriever = build_rag_chain(vector_db)

# Step 5: Ask a test question
question = "What is retrieval-augmented generation?"
print(f"\n❓ Question: {question}")
response = query_rag(retriever, question)

# Step 6: Show result
print("\n✅ Answer:")
print(response)
