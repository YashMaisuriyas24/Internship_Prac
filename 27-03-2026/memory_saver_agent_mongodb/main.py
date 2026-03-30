import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pymongo import MongoClient
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from pymongo.errors import ConnectionFailure


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
SESSION_ID = "user_session_1"

client = MongoClient(os.getenv("MONGO_URI"))


try:
    client.admin.command('ping')
    print(" Successfully connected to MongoDB")
except ConnectionFailure as e:
    print(f" Could not connect to MongoDB: {e}")
except Exception as e:
    print(f" An unexpected error occurred: {e}")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("GROQ_MODEL"),
    temperature=0.3
)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm


def get_messages_history(session_id: str):
    # 1. Connect to Long-term Storage (MongoDB)
    history = MongoDBChatMessageHistory(
        connection_string=MONGO_URI,
        session_id=session_id,
        database_name="langchain_db",
        collection_name="chat_history"
    )

    all_msgs = history.messages

    if len(all_msgs) > 4:

        short_term_context = all_msgs[:2] + all_msgs[-2:]
        history.clear()
        history.add_messages(short_term_context)

    return history


chatbot = RunnableWithMessageHistory(
    chain,
    get_messages_history,
    input_messages_key="input",
    history_messages_key="history",
)

print("Groq Chat Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = chatbot.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": SESSION_ID}}
    )


    print(f"AI: {response.content}")
