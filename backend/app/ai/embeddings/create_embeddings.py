from pathlib import Path
import chromadb

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

WHO_DIR = BASE_DIR / "knowledge_base" / "who"
FSSAI_DIR = BASE_DIR / "knowledge_base" / "fssai"

VECTOR_DB = BASE_DIR / "vector_db"


# ---------------------------------------------------
# Embedding Model
# ---------------------------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ---------------------------------------------------
# Text Splitter
# ---------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=100
)


# ---------------------------------------------------
# ChromaDB
# ---------------------------------------------------

client = chromadb.PersistentClient(path=str(VECTOR_DB))

collection = client.get_or_create_collection(
    name="nutrition_knowledge"
)


# ---------------------------------------------------
# Read Markdown Files
# ---------------------------------------------------

documents = []


def load_documents(folder, source):

    for file in folder.glob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        chunks = text_splitter.split_text(text)

        for chunk in chunks:

            documents.append(

                {
                    "text": chunk,
                    "source": source,
                    "filename": file.name
                }

            )


load_documents(
    WHO_DIR,
    "WHO"
)

load_documents(
    FSSAI_DIR,
    "FSSAI"
)


print(f"Loaded {len(documents)} chunks")


# ---------------------------------------------------
# Generate Embeddings
# ---------------------------------------------------

for i, doc in enumerate(documents):

    embedding = embedding_model.encode(
        doc["text"]
    ).tolist()

    collection.add(

        ids=[str(i)],

        embeddings=[embedding],

        documents=[doc["text"]],

        metadatas=[

            {

                "source": doc["source"],

                "file": doc["filename"]

            }

        ]

    )


print("=" * 50)

print("Knowledge Base Created Successfully!")

print("Total Chunks:", len(documents))

print("=" * 50)