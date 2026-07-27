import os

from app.models.document import Document
from app.pdf.pdf_reader import PDFReader
from app.pdf.text_splitter import TextSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.embeddings.vector_store import VectorStore
from app.embeddings.semantic_search import SemanticSearch


class PDFManager:

    def __init__(self):
        self.documents = []
        self.reader = PDFReader()
        self.splitter = TextSplitter()
        self.embedding = EmbeddingModel()
        self.vector_store = VectorStore()
        self.semantic_search = SemanticSearch()
    
    def semantic_search(self, query):
        query_embedding = self.embedding_model.embed(query)
        results = self.semantic_search.search(
            query_embedding,
            self.vector_store
        )
        return results    
        
    def load_document(self, file_path):
        for document in self.documents:
            if document.path == file_path:
                return document
        text = self.reader.read_pdf(file_path)
        chunks = self.splitter.split_text(text)
        document = Document(
            name=os.path.basename(file_path),
            path=file_path,
            text=text,
            chunks=chunks
        )
        self.documents.append(document)
        return document        
    
    def get_documents(self):
        return self.documents
    
    def remove_document(self, document):
        if document in self.documents:
            self.documents.remove(document)
    
    def clear_documents(self):
        self.documents.clear()     
     
    def search_documents(self, query, searcher):
        results = []
        for document in self.documents:
            matches = searcher.search(
                document.chunks,
                query
            )
            results.extend(matches)
        return results       