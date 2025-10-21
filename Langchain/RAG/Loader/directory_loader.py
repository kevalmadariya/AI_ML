from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = '../../ExtraData/',
    glob='**/*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(f'Total number of documents: {len(docs)}')
print(f'Document type : {type(docs)}')
print(f'Entry type : {type(docs[0])}')
print(docs[0].metadata)
print(docs[0].page_content)

