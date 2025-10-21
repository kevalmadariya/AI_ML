from langchain_core.runnables import  RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
from dotenv import load_dotenv

load_dotenv()

def pick_best_movie(movies: str) -> str:
    movie_list = movies.split('\n')
    return movie_list[0] if movie_list else "No movies provided"

runnable_function = RunnableLambda(pick_best_movie)

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

property_1 = PromptTemplate(
    template = 'Suggest me only 3 hollywood movie name of genre {topic}.nothing else',
    input_variables=['topic'] 
)

parser = StrOutputParser()

chain = RunnableSequence(property_1, model, parser)

parallel_chain = RunnableParallel({
    'movies name': RunnablePassthrough(),
    'selected movie': runnable_function
})

final_chain = chain | parallel_chain

result = final_chain.invoke({'topic':'2025 Anime'})

print(result)


