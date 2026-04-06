from langgraph.graph import StateGraph, START,END;
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import GoogleGenerativeAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os

load_dotenv()

api_key =os.getenv("GOOGLE_GEMINIUS_API_KEY")

llm = GoogleGenerativeAI(model="gemini-1.5-flash-preview", temperature=0.7, google_api_key=api_key)

class ChatState(TypedDict):
   messages : Annotated[list[BaseMessage],add_messages] 


def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
