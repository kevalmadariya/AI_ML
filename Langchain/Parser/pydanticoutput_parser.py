import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()


# ✅ Use a model that works with Hugging Face free Inference API
client = InferenceClient(
    model="google/flan-t5-large",  # works free
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")  # must be set in .env
)


# ---- Pydantic schema ----
class MovieInfo(BaseModel):
    name: str = Field(description="Name of the movie")
    about: str = Field(description="Short description of the movie")
    imdb: str = Field(description="IMDb rating of the movie")


class MoviesList(BaseModel):
    movies: list[MovieInfo]


parser = PydanticOutputParser(pydantic_object=MoviesList)


# ---- Prompt ----
template = PromptTemplate(
    template=(
        "Suggest 3 best hollywood movies related to this {topic} genre.\n"
        "Return ONLY valid JSON.\n"
        "{format_instructions}"
    ),
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


prompt = template.invoke({"topic": "Horror"})


# ---- Query ----
result = client.text_generation(prompt, max_new_tokens=300)


print("Raw output:\n", result)


# ---- Parse into Pydantic ----
final_result = parser.parse(result)
print("\nParsed result:\n", final_result)
