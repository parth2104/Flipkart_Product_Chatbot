import os
from dotenv import load_dotenv
load_dotenv()



class Config:
    OPENAI_API_KEY=os.getenv("openai_api_key")
    ENDPOINT=os.getenv("endpoint")
    HF_TOKEN=os.getenv("HF_Token")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    RAG_MODEL="llama-3.3-70b-versatile"
    EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
    ASTRA_DB_TOKEN=os.getenv("Astra_db_Token")
    ASTRA_DB_ENDPOINT=os.getenv("Astra_db_End_Point")
    ASTRA_DB_KEY_SPACE=os.getenv("Astra_db_Keyspace")