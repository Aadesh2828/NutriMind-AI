from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent
VECTOR_DB = BASE_DIR / "vector_db"

client = chromadb.PersistentClient(path=str(VECTOR_DB))

collection = client.get_collection("nutrition_knowledge")

query = input("Ask a nutrition question: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\n" + "="*60)

for i, doc in enumerate(results["documents"][0]):

    print(f"\nResult {i+1}\n")

    print(doc)

    print("\nSource:", results["metadatas"][0][i]["source"])

    print("-"*60)