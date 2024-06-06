from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 

def extract_data(data):
    loder=DirectoryLoader(data,
                          glob="*.pdf",
                          loader_cls=PyPDFLoader)
    
    documents=loder.load()

    return documents

def split_data(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks=text_splitter.split_documents(extracted_data)

    return text_chunks

def download_hugging_face_embedding():
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    return embedding
