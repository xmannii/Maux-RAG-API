# in this example we will initialize the vector database and add some documents to it
import requests


BASE_URL = "http://localhost:8000/v1"

def initialize_collection():
    response = requests.post(f"{BASE_URL}/vector_db/initialize_collection")
    print(response.json())

# if you want to add multiple documents you can use the following function
#def add_documents():
   
    #docs=[
    #    {"text": "ماکس یک پلتفرم جامع برای استفاده از هوش مصنوعی است " , "metadata": {"source": "faq"}},
    #    {"text": "ماکس یک پلتفرم جامع برای استفاده از هوش مصنوعی است " , "metadata": {"source": "faq"}},
    #    {"text": "ماکس یک پلتفرم جامع برای استفاده از هوش مصنوعی است " , "metadata": {"source": "faq"}},
    #]
    # for doc in docs:  
    #     response = requests.post(f"{BASE_URL}/vector_db/add_document", json=doc)
    #     print(response.json())

def add_document():
    response = requests.post(f"{BASE_URL}/vector_db/add_document", json={"text": "ماکس یک پلتفرم جامع برای استفاده از هوش مصنوعی است " , "metadata": {"source": "faq"}})
    print(response.json())



initialize_collection()
add_document()