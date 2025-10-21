from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

input = """
neg_prompt = PromptTemplate(
    template = 'Write an 3 lines of appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

pos_prompt = PromptTemplate(
    template = 'Write an 3 lines of appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

#chians
classifier_chain = prompt1 | model_google | parser2

brach_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive' , pos_prompt | model_gpt2 | parser1),
    (lambda x: x.sentiment == 'negative' , neg_prompt | model_gpt2 | parser1),
    RunnableLambda(lambda x: "Could not find sentiment")
)

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0,    
)

chunks = splitter.split_text(input)

print(f'Total Chunks: {len(chunks)}')
print(chunks[1])