from langchain_huggingface import HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import RunnableBranch, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal


load_dotenv()


#schema
class Feedback(BaseModel):


    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of feedback')


#models
model_google = ChatGoogleGenerativeAI(model='gemini-2.5-pro')


model_gpt2 = HuggingFacePipeline.from_model_id(model_id='gpt2', task='text-generation')


#parsers
parser1 = StrOutputParser()


parser2 = PydanticOutputParser(pydantic_object=Feedback)


#prompts
prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback} {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction' : parser2.get_format_instructions()}
)


neg_prompt = PromptTemplate(
    template = 'Write an 3 lines of appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


pos_prompt = PromptTemplate(
    template = 'Write an 3 lines of appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)


#chians
classifier_chain = prompt1 | model_google | parser2


brach_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive' , pos_prompt | model_gpt2 | parser1),
    (lambda x: x.sentiment == 'negative' , neg_prompt | model_gpt2 | parser1),
    RunnableLambda(lambda x: "Could not find sentiment")
)


chain = classifier_chain | brach_chain


print(chain.invoke({'feedback':'The movie is to slow and i slept while watching it.'}))


chain.get_graph().print_ascii()

