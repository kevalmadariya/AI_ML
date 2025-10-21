from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


doc = ["King","Card"]
q = "Black"


phrase_embedding = embedding.embed_documents(doc)
query_embedding = embedding.embed_query(q)


scores = cosine_similarity([query_embedding],phrase_embedding)[0]


print(scores)
