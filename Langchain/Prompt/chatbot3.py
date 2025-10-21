from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv


load_dotenv()


model = HuggingFacePipeline.from_model_id(model_id="gpt2",task="text-generation")


chat_history = [
    SystemMessage(content="You are Movie Director")
]


while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI: ",result)


print(chat_history)
