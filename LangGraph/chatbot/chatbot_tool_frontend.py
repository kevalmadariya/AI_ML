import streamlit as st
from chatbot_tool_backend import chatbot, get_thread_ids
from langchain_core.messages import HumanMessage, AIMessage ,ToolMessage
import uuid

#==========================  utility function =======================

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_chat_thread(thread_id)
    st.session_state['message_history'] = []
    return thread_id

def add_chat_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

def load_history(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])


#===========================     sessions      ============================

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread'] = get_thread_ids()
    add_chat_thread(st.session_state['thread_id'])

#===========================  configuration ===========================

CONFIG = {'configurable' : {'thread_id' : st.session_state['thread_id']}}



#============================    Side bar       ==========================

st.sidebar.title('ChatBot')

if st.sidebar.button('New Chat'):
    reset_chat()
    
st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_thread'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
    
        messages = load_history(thread_id)
        
        temp_messages = []

        for msg in messages:
            
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            
            temp_messages.append({'role': role , 'message' : msg.content})
            
        st.session_state['message_history'] = temp_messages

#===========================     main UI    ============================

for i in st.session_state['message_history']:
    with st.chat_message(i['role']):
          st.text(i['message'])
    
user_input = st.chat_input('Type hear')

if user_input:

    st.session_state['message_history'].append({'role':'user' , 'message' : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {"thread_id": st.session_state["thread_id"]},
        "run_name": "chat_turn",
    }
    # # response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config = CONFIG)
    # # ai_replay = response['messages'][-1].content
    # # st.session_state['message_history'].append({'role':'assistant' , 'message' : ai_replay})
    # with st.chat_message('assistant'):
    #     ai_assistent = st.write_stream(
    #       message_chunk.content for message_chunk, metadata in chatbot.stream(
    #           {'messages':[HumanMessage(content=user_input)]}, 
    #           config = CONFIG,
    #           stream_mode= 'messages'
    #       )
    #     )
    #     st.session_state['message_history'].append({'role':'assistant' , 'message' : ai_assistent})
    
    # Assistant streaming block
    with st.chat_message("assistant"):
        # Use a mutable holder so the generator can set/modify it
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                # Lazily create & update the SAME status container when any tool runs
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )

                # Stream ONLY assistant tokens
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

    # Save assistant message
    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message}
    )
