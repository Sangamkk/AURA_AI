class VectorStore:

    def __init__(self):

        self.vectors = []

    def add(self, embedding, chunk):

        self.vectors.append(
            (embedding, chunk)
        )

    def get_all(self):

        return self.vectors