from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set GOOGLE_API_KEY in your environment")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


result = llm.invoke("What is the capital of India?")
print(result.content)
