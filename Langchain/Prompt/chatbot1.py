from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()


template = PromptTemplate(
    input_variables=['query','mood','response_type'],
    template="""
You are a conversational AI assistant.
The user will give you a query and also specify a mood and response style.


- Mood choices: happy, sad, angry  
- Response style choices: short, long, debate, brief  


Your task:
1. Answer the user's query in a way that reflects the selected mood.  
2. Match the response style to the requested type.  
   - short → 1–2 sentences  
   - long → a detailed explanation  
   - debate → present multiple viewpoints, pros/cons, and conclude  
   - brief → a concise, to-the-point answer  


Now respond to the following:


User Query: {query}  
Mood: {mood}  
Response Style: {response_type}  


Your Response:
"""
)


llm = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    task="conversational",
    max_new_tokens=10
)


model = ChatHuggingFace(llm=llm)


st.header('ChatBot')


query = st.text_input("Enter one line Query")


mood = st.selectbox("Select Response Mood😄",["happy", "sad", "angry"])


response_type = st.selectbox("Select Response type",["short", "long", "debate", "brief"])


prompt = template.invoke({
     'query': query,
     'mood': mood,
     'response_type': response_type
})


if st.button('Generate'):
    result = model.invoke(prompt)
    st.text(result.content)