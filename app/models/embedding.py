from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    text: str
    metadata: Optional[dict] = None

class Query(BaseModel):
    prompt: str

class SearchResult(BaseModel):
    id: int
    text: str
    metadata: Optional[dict] = None


class EmbeddingResponse(BaseModel):
    embedding: List[float]