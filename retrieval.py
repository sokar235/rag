def basic_search(vector_db, query, k=3):
    results = vector_db.similarity_search(query, k=k)
    for doc in results:
        print(f">>> {doc.metadata} — {doc.page_content[:200]}...\n")
    return results
