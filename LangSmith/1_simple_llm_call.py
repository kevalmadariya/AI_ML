from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


prompt = PromptTemplate(
    template = 'Suggest me only 2 hollywood movie name of genre {topic}',
    input_variable = ['topic']
)


model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')


parser = StrOutputParser()


chain = prompt | model | parser


result = chain.invoke({'topic':'Horror'})


print(result)


chain.get_graph().print_ascii()
