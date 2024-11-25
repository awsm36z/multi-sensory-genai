import os
from dotenv import load_dotenv

def load_my_api_key():
    load_dotenv()
    apiKey = os.getenv("OPENAI_API_KEY")
    return apiKey