from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# It's good practice to load environment variables, though not strictly needed for this specific script
load_dotenv()

documents = [
    Document(page_content="Demon Slayer is a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows Tanjiro Kamado, a kind"),
    Document(page_content="Inception is a 2010 science fiction action film written and directed by Christopher Nolan. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious of his targets."),
    Document(page_content="Dark is a German science fiction thriller streaming television series co-created by Baran bo Odar and Jantje Friese. It is the first German-language Netflix original series."),
    Document(page_content="Space Exploration refers to the ongoing discovery and exploration of celestial structures in outer space by means of continuously evolving and growing space technology."),
    Document(page_content="Money Heist is a Spanish heist crime drama television series created by Álex Pina. The series traces two long-prepared heists led by the Professor (Álvaro Morte).")
]

# 1. CORRECTED: Initialize the embedding model using the LangChain wrapper
# This wrapper makes the sentence-transformer model compatible with LangChain components like Chroma.
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_function = HuggingFaceEmbeddings(model_name=model_name)

# 2. CORRECTED: Pass the LangChain embedding object to Chroma
# The `embedding` parameter now receives the correctly wrapped model.
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_function, # Use the wrapped embedding function here
    collection_name="my_collection"
)

# The rest of your code is correct and remains the same
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "Space and Science fiction series"
results = retriever.invoke(query)

print(f"Query: '{query}'")
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---\n: {doc.page_content}\n----")