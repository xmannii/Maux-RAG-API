from app.models.chat import ChatResponse, ChatCompletionMessage, Choice, CompletionUsage

def map_chat_response(response):
    return ChatResponse(
        id=response.id,
        created=response.created,
        model=response.model,
        choices=[
            Choice(
                finish_reason=choice.finish_reason,
                index=choice.index,
                message=ChatCompletionMessage(
                    content=choice.message.content,
                    role=choice.message.role,
                    function_call=choice.message.function_call,
                    tool_calls=choice.message.tool_calls,
                    refusal=choice.message.refusal
                )
            )
            for choice in response.choices
        ],
        usage=CompletionUsage(
            completion_tokens=response.usage.completion_tokens,
            prompt_tokens=response.usage.prompt_tokens,
            total_tokens=response.usage.total_tokens
        ),
        service_tier=response.service_tier,
        system_fingerprint=response.system_fingerprint
    )