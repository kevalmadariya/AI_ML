from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

os.environ['LANGCHAIN_PROJECT'] = 'sequenctial demo'

load_dotenv()

model1 = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

model2 = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

prompt1 = PromptTemplate(
    template = 'Suggest me only 3 hollywood movie name of genre {topic}.nothing else',
    input_variables=['topic']
)


pick_one = PromptTemplate(
    template = 'Pick only one name out of following movies \n {movies}',
    input_variables=['movies']
)


parser = StrOutputParser()


chain = prompt1 | model1 | parser | pick_one | model2 | parser

config = {
    'run_name' : 'RunnableSequence',
    'tags' : ['llm app' , 'movie suggesion'],
    'metadata' : {'model1' : 'gemini-2.5-pro' , 'output parser' : 'StdOutput'
    }
}

result = chain.invoke({'topic':'Spy'} , config=config)


print(result)
