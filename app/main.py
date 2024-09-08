from fastapi import FastAPI
from app.routes import vector_db, chat
import logging


app = FastAPI(title="RAG API", description="API for RAG operations using Milvus and OpenAI")
logging.basicConfig(level=logging.INFO)
logging.info("API STARTED. PLEASE CALL THE /V1/VECTOR_DB/INITIALIZE_COLLECTION FIRST TO INITIALIZE THE COLLECTION")


# Include routers with v1 prefix and tags
app.include_router(vector_db.router, prefix="/v1/vector_db", tags=["Vector Database"])
app.include_router(chat.router, prefix="/v1/chat", tags=["Chat"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the RAG API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)