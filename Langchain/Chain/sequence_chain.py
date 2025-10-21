from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()


model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')


prompt1 = PromptTemplate(
    template = 'Suggest me only 3 hollywood movie name of genre {topic}.nothing else',
    input_variables=['topic']
)


pick_one = PromptTemplate(
    template = 'Pick only one name out of following movies \n {movies}',
    input_variables=['movies']
)


parser = StrOutputParser()


chain = prompt1 | model | parser | pick_one | model | parser


result = chain.invoke({'topic':'Sci-fi'})


print(result)


chain.get_graph().print_ascii()


