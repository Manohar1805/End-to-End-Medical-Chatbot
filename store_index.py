from src.helper import extract_data, split_data, download_hugging_face_embedding
from dotenv import load_dotenv
import os
from pinecone import Pinecone  # Correct import
from langchain_community.vectorstores import Pinecone as store


# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
# PINECONE_API_KEY="37492372-5eea-42a2-9bed-e8cf8ec108e2"
PINECONE_ENV = os.getenv("PINECONE_ENV")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Extract and split data
extracted_data = extract_data("data/")
chunks = split_data(extracted_data)
print(f"length of chunks is {len(chunks)}")

# Download embeddings
embeddings = download_hugging_face_embedding()

# Creating Pinecone index and storing embeddings
index_name = "chatbot"

# Ensure the index exists, create if it does not
if index_name not in pc.list_indexes().names():
    pc.create_index(index_name, dimension=embeddings.dim)

index = pc.Index(index_name)

# Creating Embeddings for Each of The Text Chunks & storing
docsearch = store.from_texts([t.page_content for t in chunks], embeddings, index_name=index_name)
