# in this example we will now use the /chat/completions endpoint to chat with our RAG System
import requests
import json

BASE_URL = "http://localhost:8000/v1"

def completions_chat():
    response = requests.post(f"{BASE_URL}/chat/completions", json={"prompt": "ماکس چیه؟"})
    response_data = response.json()
    
    # Extract and print only the content
    content = response_data['choices'][0]['message']['content']
    print(content)

completions_chat()