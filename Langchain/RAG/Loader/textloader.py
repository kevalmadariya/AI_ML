from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path='../../ExtraData/mobiledata.txt', encoding='utf8')

docs = loader.load()

print(f'Total number of documents: {len(docs)}')
print(f'Document type : {type(docs)}')
print(f'Entry type : {type(docs[0])}')
print(docs[0])