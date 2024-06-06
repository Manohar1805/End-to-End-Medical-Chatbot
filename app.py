from flask import Flask, render_template,jsonify,request
from src.helper import download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone as store
import pinecone
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms.ctransformers import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "chatbot"

# # Ensure the index exists, create if it does not
# if index_name not in pc.list_indexes().names():
#     pc.create_index(index_name, dimension=embeddings.dim)

# index = pc.Index(index_name)

app=Flask(__name__)

embeddings=download_hugging_face_embedding()

doc_search=store.from_existing_index(index_name,embeddings)

PROMPT=PromptTemplate(template=prompt_template,input_variables=["context","question"])

chain_type_kwargs={"prompt":PROMPT}

llm=CTransformers(model="Models\llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={"max_new_tokens":512,
                          "temperature":0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=doc_search.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs
)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    result=qa({"query":input})
    print("response : ",result['result'])
    return str(result['result'])

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)