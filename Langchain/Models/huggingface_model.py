from langchain_huggingface import HuggingFacePipeline
import os


os.environ['HF_HOME'] = 'C:/huggingface_cache'


llm = HuggingFacePipeline.from_model_id(
    #   model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
      model_id = 'gpt2',
      task='text-generation',
)


result = llm.invoke("What is demon?")


print(result)
