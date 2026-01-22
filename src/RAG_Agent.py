from langchain_groq.chat_models import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool

from src.config import Config


def build_flipkart_retriever_tool(retriever):

    @tool
    def flipkart_retriever_tool(query: str) -> str:
        """
        Retrieve Flipkart product reviews related to the user query.
        """
        docs = retriever.invoke(query)
        return "\n\n".join(doc.page_content for doc in docs)

    return flipkart_retriever_tool

class RAGAgentBuilder:

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.model = ChatGroq(model=Config.RAG_MODEL,  temperature=0)

    def build_agent(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        flipkart_tool = build_flipkart_retriever_tool(retriever)

        agent = create_agent(
            model= self.model,
            tools=[flipkart_tool],
            system_prompt="""
You are an e-commerce assistant for Flipkart.
You answer questions strictly using product reviews and titles.

RULES:
- Always use the flipkart_retriever_tool to find answers.
- If the answer is not found in reviews, say:
  "I don't know the answer. Please contact customer care at +0000000000"
""",
            checkpointer=InMemorySaver()
        )

        return agent




