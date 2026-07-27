from app.embeddings.similarity import Similarity
class SemanticSearch:
    def search(self,query_embedding,vector_store):
        results = []
        for embedding, chunk in vector_store.get_all():
            score = Similarity.cosine(
                query_embedding,
                embedding
            )
            results.append(
                (score, chunk)
            )
        results.sort(reverse=True)
        return results[:5]