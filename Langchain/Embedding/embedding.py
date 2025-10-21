from sentence_transformers import SentenceTransformer, util

# 1. Load the pre-trained model
# The model will be downloaded automatically the first time you run this.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 2. Define a list of sentences you want to embed
sentences = [
    "A man is eating food.",
    "A man is eating a piece of bread.",
    "The girl is carrying a baby.",
    "A man is riding a horse.",
    "The sky is blue and the sun is bright."
]

# 3. Generate the embeddings for the sentences
embeddings = model.encode(sentences)

# The result 'embeddings' is a NumPy array with a shape of (5, 384)
# 5 sentences, and each embedding has a dimension of 384.
print("Shape of embeddings:", embeddings.shape)
print("-" * 30)

# 4. (Optional) Calculate cosine similarity between the first two sentences
# Cosine similarity is a measure of how similar two vectors are.
# A value of 1 means they are identical, 0 means they are unrelated.
similarity = util.cos_sim(embeddings[0], embeddings[1])

print(f"Sentences:\n- {sentences[0]}\n- {sentences[1]}")
print("Similarity score:", similarity[0][0].item()) # .item() gets the Python number