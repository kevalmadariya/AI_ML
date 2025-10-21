from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should return False

load_dotenv()

#model
model_google = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

#parser
parser = StrOutputParser()  

#prompt
prompt = PromptTemplate(
    template = 'Suggest me only one movie name of genre \n {genre}',
    input_variables=['genre']
)   

#runnable
sequential_runnable = RunnableSequence(prompt, model_google, parser)

print(sequential_runnable.invoke({'genre': 'time travel'}))