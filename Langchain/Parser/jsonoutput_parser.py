from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda


load_dotenv()


# Use "conversational" instead of "text-generation"
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational"
)


model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()


template = PromptTemplate(
    template = 'Suggest me best anime movie \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


prompt = template.format()


result = model.invoke(prompt)
print(result)


final_result = parser.parse(result.content)
print(final_result)
