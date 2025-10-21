from langchain_community.retrievers.wikipedia import WikipediaRetriever
from dotenv import load_dotenv

load_dotenv()

wikipedia_retriever = WikipediaRetriever(
    top_k=2,
    lang='en'
)

query = "Inception Movie"

docs = wikipedia_retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n---Document {i+1}---:\n")
    print(doc.page_content)