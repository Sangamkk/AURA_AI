class Similarity:

    @staticmethod
    def cosine(query, embedding):
        return len(
            set(query) &
            set(embedding)
        )