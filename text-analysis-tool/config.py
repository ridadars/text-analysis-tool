# config.py
import os
from dotenv import load_dotenv

# Load values from .env into environment
load_dotenv()

# Access your API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# (Optional) raise error if not set
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY. Please set it in .env file.")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY. Please set it in .env file.")
