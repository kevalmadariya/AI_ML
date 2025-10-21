from langchain_community.document_loaders import WebBaseLoader
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

url='https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'

loader = WebBaseLoader(url)

docs = loader.load()

print(f'Total number of documents: {len(docs)}')
print(f'Document type : {type(docs)}')
print(f'Entry type : {type(docs[0])}')
print(docs[0].metadata)
print(docs[0].page_content)