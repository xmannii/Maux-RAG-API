from pydantic import BaseModel
from typing import List, Optional

class ChatCompletionMessage(BaseModel):
    content: str
    role: str
    function_call: Optional[dict] = None
    tool_calls: Optional[List[dict]] = None
    refusal: Optional[dict] = None

class Choice(BaseModel):
    finish_reason: str
    index: int
    logprobs: Optional[dict] = None
    message: ChatCompletionMessage

class CompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class ChatResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[Choice]
    usage: CompletionUsage
    service_tier: Optional[str] = None
    system_fingerprint: Optional[str] = None
