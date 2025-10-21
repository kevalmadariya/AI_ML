from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


load_dotenv()


# Use "conversational" instead of "text-generation"
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational"
)


model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


# detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)


# summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{report}",
    input_variables=["report"]
)


# Helper to wrap parser output into dict
def to_dict(text: str) -> dict:
    return {"report": text}


chain = (
    template1
    | model
    | parser
    | RunnableLambda(to_dict)
    | template2
    | model
    | parser
)


result = chain.invoke({"topic": "black hole"})
print(result)
