import streamlit as st

with st.chat_message('user'):
    st.text('hii')

with st.chat_message('assistant'):
    st.text('I am AI')

user_input = st.chat_input('Type hear')

if user_input:
    with st.chat_message('user'):
        st.text(user_input)