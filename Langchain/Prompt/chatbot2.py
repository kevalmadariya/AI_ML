from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    max_new_tokens=3,
    task='conversational',
    streaming=True,  
)


model = ChatHuggingFace(llm=llm)


while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)
