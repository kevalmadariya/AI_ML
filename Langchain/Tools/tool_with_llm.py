from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

llm_with_tools = llm.bind_tools([multiply_numbers])

query = HumanMessage("What is the product of 6 and 7?")

messages = [query]

result = llm_with_tools.invoke(messages)

messages.append(result)

print(f"LLM Response: {result}")
print("\n---Messages---\n")
print(messages)

print("\n---Tool Message---\n")

tool_message = multiply_numbers.invoke(result.tool_calls[0])
print(tool_message)

messages.append(tool_message)
print("\n---Messages---\n")
print(messages)

print("\n---Final LLM Response---\n")

print(llm_with_tools.invoke(messages).content)