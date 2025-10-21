from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough 

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

prompt1 = PromptTemplate(
    template = 'Suggest me only 3 hollywood movie name of genre {topic}.nothing else',
    input_variables=['topic']
)

pick_one = PromptTemplate(
    template = 'Pick best movie out of following movies \n {movies}',
    input_variables=['movies']
)

parser = StrOutputParser()

first_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'movies name': RunnablePassthrough(),
    'selected movie': RunnableSequence(pick_one, model, parser)
})  

final_chain = first_chain | parallel_chain

result = final_chain.invoke({'topic':'Anime'})

print(result)

final_chain.get_graph().print_ascii()


