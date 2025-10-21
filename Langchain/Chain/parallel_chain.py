from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel  # ✅ FIXED

load_dotenv()

model1 = HuggingFacePipeline.from_model_id(model_id='gpt2', task='text-generation')
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

prompt1 = PromptTemplate(
    template='Suggest me just 1 hollywood movies of genre {genre1}.nothing else',
    input_variables=['genre1'],
)

prompt2 = PromptTemplate(
    template='Suggest me just 1 hollywood movies of genre {genre2}.nothing else',
    input_variables=['genre2'],
)

prompr3 = PromptTemplate(
    template='make sentence using following words: \n {genre1} , {genre2}',
    input_variables=['genre1', 'genre2']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'genre1': prompt1 | model1 | parser,
    'genre2': prompt2 | model2 | parser
})

merge_chain = prompr3 | model2 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'genre1': 'Sci-fi', 'genre2': 'Spy'})

print(result)

chain.get_graph().print_ascii()
