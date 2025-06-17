# Directory: src/config/settings.py
from pydantic_settings import BaseSettings
from pydantic import AnyUrl

class Settings(BaseSettings):
    groq_api_key: str
    weaviate_url: AnyUrl
    model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"

settings = Settings()

