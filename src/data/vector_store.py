import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from models.llm_model import get_ollama_embedding_model

OFFERS_PATH = os.path.join(os.path.dirname(__file__), "offers.txt")  

class FaiisVectorStore:
    def __init__(self):
        chunks = self._load_and_split_offers()
        self.vector_store = self._create_faiss_vector_store(chunks)

    def _load_and_split_offers(self):
        # Load the file as a single document
        loader = TextLoader(OFFERS_PATH, encoding='utf-8')
        docs = loader.load()
        # Use MarkdownHeaderTextSplitter to split on '## ' headers
        splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("##", "destination")])
        # Split the document into chunks (destinations)
        raw_chunks = splitter.split_text(docs[0].page_content)
        # Add destination info to both page_content and metadata
        chunks = []
        for chunk in raw_chunks:
            destination = chunk.metadata.get('destination', '').strip()
            # Prepend destination info to page_content for better retrieval
            chunk.page_content = f"Destination: {destination}\n  Offers:  {chunk.page_content.strip()}"
            # Also ensure destination is in metadata
            chunk.metadata['destination'] = destination
            chunks.append(chunk)
        return chunks

    # Function to create embeddings and store in FAISS
    def _create_faiss_vector_store(self, chunks):
        # Use Ollama's nomic-embed-text:v1.5 embedding model from central model provider
        embeddings = get_ollama_embedding_model()
        # Create FAISS vector store
        vector_store = FAISS.from_documents(chunks, embeddings)
        return vector_store
    
    def get_vector_store(self):
        """
        Returns the FAISS vector store instance.
        """
        return self.vector_store