import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

thread_id = 1
CONFIG = {'configurable' : {'thread_id' : thread_id}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for i in st.session_state['message_history']:
    with st.chat_message(i['role']):
          st.text(i['message'])
    
user_input = st.chat_input('Type hear')


if user_input:

    st.session_state['message_history'].append({'role':'user' , 'message' : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config = CONFIG)
    # ai_replay = response['messages'][-1].content
    # st.session_state['message_history'].append({'role':'assistant' , 'message' : ai_replay})
    with st.chat_message('assistant'):
        ai_assistent = st.write_stream(
          message_chunk.content for message_chunk, metadata in chatbot.stream(
              {'messages':[HumanMessage(content=user_input)]}, 
              config = CONFIG,
              stream_mode= 'messages'
          )
        )
        st.session_state['message_history'].append({'role':'assistant' , 'message' : ai_assistent})
