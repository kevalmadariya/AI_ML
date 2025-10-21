from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='../../ExtraData/sample.csv', encoding='utf-8')

docs = loader.load()

print(f'Total number of documents: {len(docs)}')
print(f'Document type : {type(docs)}')
print(f'Entry type : {type(docs[0])}')
print(docs[0].metadata)
print(docs[0].page_content)