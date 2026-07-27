class EmbeddingManager:

    def __init__(self):
        self.embeddings = []

    def add_embedding(self, chunk, vector):

        self.embeddings.append({
            "chunk": chunk,
            "vector": vector
        })

    def get_embeddings(self):

        return self.embeddings

    def clear(self):

        self.embeddings.clear()