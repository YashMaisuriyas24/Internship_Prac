import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_mongodb import MongoDBChatMessageHistory
from pymongo import MongoClient
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
client = MongoClient(os.getenv("MONGO_URI"))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=GROQ_API_KEY
)

session_id = "user_session_1"
mongo_memory = MongoDBChatMessageHistory(
    connection_string=MONGO_URI,
    session_id=session_id,
)

SYSTEM_PROMPT = """
You are a professional AI assistant that keeps track of the conversation. 
Guidelines:
1. Maintain context using short-term memory (last 4 exchanges fully visible).
2. Retrieve older messages from long-term memory (MongoDB) when needed.
3. Answer clearly and naturally, human-like.
4. Recall previous questions and answers accurately. For example:
   User: What is 2+2?
   AI: 2+2 equals 4.
   User: What was my first question?
   AI: Your first question was "What is 2+2?", and the answer was "4".
5. If an answer is not found in any memory, respond politely indicating lack of information.
"""

@tool
def your_read_email_tool(email_id: str) -> str:
    return f"Email content for ID: {email_id}"

@tool
def your_send_email_tool(recipient: str, subject: str, body: str) -> str:
    return f"Email sent to {recipient} with subject '{subject}'"

agent = create_agent(
    model=llm,
    tools=[your_read_email_tool, your_send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "your_send_email_tool": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                },
                "your_read_email_tool": False,
            }
        ),
    ],
)

def update_long_term(local_messages):
    if len(local_messages) > 8:
        old = local_messages[:-8]
        for msg in old:
            mongo_memory.add_message(msg)
        return local_messages[-8:]
    return local_messages

def search_long_term(query):
    for msg in reversed(mongo_memory.messages):
        if query.lower() in msg.content.lower():
            return msg
    return None

def chat():
    thread_id = "rag_thread_1"
    local_messages = [SystemMessage(content=SYSTEM_PROMPT)]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        prompt_message = HumanMessage(content=user_input)

        retrieved_msg = search_long_term(user_input)
        if retrieved_msg:
            prompt_message.content += f"\nRelevant old memory: {retrieved_msg.content}"

        result = agent.invoke(
            {"messages": local_messages + [prompt_message]},
            config={"configurable": {"thread_id": thread_id}}
        )

        response = result["messages"][-1].content
        print("\nAI:", response)

        local_messages.append(HumanMessage(content=user_input))
        local_messages.append(AIMessage(content=response))

        local_messages = update_long_term(local_messages)

if __name__ == "__main__":
    chat()