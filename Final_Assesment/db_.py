from pymongo import MongoClient
from langchain_ollama import ChatOllama


client = MongoClient("mongodb://localhost:27017/")

collection = client["chatdb"]["history"]

collection.insert_one(

    {
        "message": "welcome to my world"
    }
)


llm = ChatOllama(
    model= "llama3.2:latest",
    temprature = 0.7,
    base_url = "http://172.16.1.224:11434/api/generate"
)


