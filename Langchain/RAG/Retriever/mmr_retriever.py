from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

documents = [
    # Cluster 1: Documents about cats (very similar to each other)
    Document(page_content="Cats are independent animals that enjoy lounging in the sun."),
    Document(page_content="Many people love cats because they are clean and quiet pets."),
    Document(page_content="Feline companions, often called cats, have been domesticated for thousands of years."),
    
    # Cluster 2: A document about dogs (relevant to the query but different from the cat documents)
    Document(page_content="Dogs are known for their loyalty and playful nature, making them great family pets.")
]

model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=model,
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2 , "lambds_mult": 0.5}) #k = 1 means no mmr effects

query = "What are popular pets?"

results = retriever.invoke(query)

print(f"Query: '{query}'")
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---\n: {doc.page_content}\n----")