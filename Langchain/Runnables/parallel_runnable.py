from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

#model
model_google = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

#parser
parser = StrOutputParser()

#prompt
prompt1 = PromptTemplate(
    template = 'Suggest me only one movie name of genre \n {genre}',
    input_variables=['genre']
)

prompt2 = PromptTemplate(
    template = 'Suggest me only one book name of genre \n {genre}',
    input_variables=['genre']
)

#runnable
parallel_runnable = RunnableParallel({
    'movie' : RunnableSequence(prompt1, model_google, parser),
    'book' : RunnableSequence(prompt2, model_google, parser)
})

print(parallel_runnable.invoke({'genre': 'stock market'}))   