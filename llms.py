from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os
from config import GEMINI_API_KEY, LANGCHAIN_API_KEY

os.environ['GOOGLE_API_KEY'] = GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=4,
    verbose=True,
    streaming=True
)

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

def langsmith_trace():
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
    os.environ['LANGCHAIN_API_KEY'] = LANGCHAIN_API_KEY
    os.environ['LANGCHAIN_PROJECT'] = 'tour_bot'