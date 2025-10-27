import streamlit as st

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

    st.session_state['message_history'].append({'role':'assistant' , 'message' : user_input})
    with st.chat_message('assistant'):
        st.text(user_input)
    
