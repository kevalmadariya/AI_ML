from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
import os
load_dotenv()


# Use a free model with text2text-generation
model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)


schema = [
    ResponseSchema(name='name', description='name of movie'),
    ResponseSchema(name='movie1', description='About Movie'),
    ResponseSchema(name='imdb', description='imdb rating of movie1'),
]


parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template=(
        "Suggest me 3 best hollywood movies related to this {topic} genre.\n"
        "{format_instruction}"
    ),
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


prompt = template.invoke({'topic': 'Horror'})


result = model.invoke(prompt)
print("Raw output:\n", result)


final_result = parser.parse(result)
print("\nParsed result:\n", final_result)
