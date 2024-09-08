from app.services.chroma_service import ChromaService
from app.services.openai_service import openai_service
import uuid
from typing import AsyncGenerator
import json
from app.config.settings import settings
class RAGService:
    def __init__(self):
        self.collection_name = "RAG_COLLECTION"
        self.chroma_service = ChromaService()

    def initialize_collection(self):
        self.chroma_service.create_collection(self.collection_name)

    def add_document(self, text: str, metadata: dict = None):
        self.chroma_service.add_documents(
            collection_name=self.collection_name,
            documents=[text],
            ids=[f"doc_{uuid.uuid4()}"],
            metadatas=[metadata] if metadata else None
        )
    def clear_collection(self):
        self.chroma_service.clear_collection(self.collection_name)
    def search_similar_documents(self, embedding: list):
        results = self.chroma_service.search(
            collection_name=self.collection_name,
            query_embeddings=embedding,
        )
        return results
    
    def generate_response(self, query: str, context: str):
        # you can change the system prompt in the env file to make the assistant more helpful based on your needs
        messages = [
            {"role": "system", "content": settings.SYSTEM_PROMPT},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
        return openai_service.create_chat_completion(messages)

     
    #TODO: create the stream route so we can use the streaming api
    async def generate_stream_response(self, prompt: str, context: str) -> AsyncGenerator[str, None]:
        try:
            stream = openai_service.create_chat_completion_stream([
                {"role": "system", "content": settings.SYSTEM_PROMPT},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
            ])
            for chunk in stream:
                yield json.dumps(chunk.model_dump()) + "\n"
            yield "[DONE]\n"
        except Exception as e:
            yield f"{json.dumps({'error': str(e)})}\n\n"

rag_service = RAGService()