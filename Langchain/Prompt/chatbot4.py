#add history also
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


chat_template = ChatPromptTemplate([
    ('system','You are a helpful {roll} expert'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','Explain in simple terms,what is {topic}')
])


chat_history = []
#load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())


prompt = chat_template.invoke({'roll':'movie','topic':'CGI'})
print(prompt)
