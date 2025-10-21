from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated , Literal, Optional


# Define schema
class Review(TypedDict):
    id: str
    summary: Annotated[list[str], "write down summary in briff"]
    sentiment: Annotated[Literal["pos","neg"],"Return sentiment of the review discussed in the review in  List"]
    name: Annotated[Optional[str],"write name of reviwer"]
# Load free local model via Ollama

llm = ChatOllama(model="mistral")  # you can also use "llama3", "gemma"

# Use structured output
structured_model = llm.with_structured_output(Review)


# Invoke with input
result = structured_model.invoke(
    "Demon Slayer: Infinity Castle delivers breathtaking animation with emotional battles and high stakes."
)


print(result)
