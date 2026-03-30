import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from tavily import TavilyClient
from langchain_core.messages import ToolMessage
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

st.title("Langchain Chatbot")
st.write("Search anything on web")

tavily_client = TavilyClient(api_key = TAVILY_API_KEY)

@tool("SearchEngine", description = "Search the queries on web")
def internet_search(query: str):
    return tavily_client.search(query)

llm = ChatGroq(
    api_key = GROQ_API_KEY,
    model = GROQ_MODEL,
    temperature = 0.3
)

model = llm.bind_tools([internet_search])

query = st.text_input("Enter your query")
result = model.invoke(query)

tool_call = result.tool_calls[0]

search_results = internet_search.invoke(tool_call["args"])

tool_message = ToolMessage(
    content = str(search_results),
    tool_call_id = tool_call["id"]
)

final_result = model.invoke([
    HumanMessage(content = query),
    result,
    tool_message
])

if query:
    st.success(final_result.content)