from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='../../ExtraData/sample.pdf')

docs = loader.load()

print(f'Total number of documents: {len(docs)}')
print(f'Document type : {type(docs)}')
print(f'Entry type : {type(docs[0])}')
print(docs[0])
