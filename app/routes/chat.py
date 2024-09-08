from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.embedding import Query
from app.models.chat import ChatResponse, ChatCompletionMessage, Choice, CompletionUsage
from app.services.rag_service import rag_service
from app.services.openai_service import openai_service
from app.services.response_service import map_chat_response
router = APIRouter()



## this route uses completion api of openai so there is no streaming and the finished response is returned
@router.post("/completions", response_model=ChatResponse)
async def generate_chat_completion(query: Query):
    try:
        prompt = query.prompt
        embedding = openai_service.create_embedding(prompt)
        search_results = rag_service.search_similar_documents(embedding)
        
        context = "Relevant documents:\n"
        for doc, metadata in zip(search_results['documents'][0], search_results['metadatas'][0]):
            context += f"- Content: {doc}\n"
            context += f"  Metadata: {metadata}\n"

        print("\033[92m" + "context injected : " + context + "\033[0m")
        response = rag_service.generate_response(prompt, context)
        
        chat_response = map_chat_response(response)
        
        return chat_response
    except Exception as e:
        print("error in completion : ", e)
        raise HTTPException(status_code=500, detail=f"Chat completion failed: {str(e)}")

        
#TODO: create the stream route so we can use the streaming api
