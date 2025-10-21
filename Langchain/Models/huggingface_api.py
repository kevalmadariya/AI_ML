import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

hf_api_key = os.getenv("HUGGINGFACE_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=hf_api_key  # Pass your token here
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke([HumanMessage(content="What is Demon Slayer?")])

print(response.content)
