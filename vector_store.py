from langchain_pinecone import PineconeVectorStore
from langchain.tools.retriever import create_retriever_tool
import os
from llms import embeddings_model
from config import PC_Key

api_key = PC_Key
store_index = 'tourdata'

def get_retriever():
    os.environ['PINECONE_API_KEY'] = api_key
    vectorstore = PineconeVectorStore(
        index_name=store_index,
        embedding=embeddings_model,
    )
    return vectorstore.as_retriever()

retriever_tool =  create_retriever_tool(
    retriever=get_retriever(),
    name='retrieve_tour_spots',
    description='useful for retrieving travel spots'
)