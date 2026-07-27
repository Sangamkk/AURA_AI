class ChunkSearcher:

    def search(self, chunks, query):

        results = []

        query = query.lower()

        for chunk in chunks:

            if query in chunk.lower():

                results.append(chunk)

        return results