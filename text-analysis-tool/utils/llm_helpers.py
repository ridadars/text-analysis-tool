# utils/llm_helpers.py
import google.generativeai as genai
from groq import Groq
from config import GEMINI_API_KEY, GROQ_API_KEY
from textblob import TextBlob
from langdetect import detect
from transformers import AutoTokenizer

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Configure Groq
groq_client = Groq(api_key=GROQ_API_KEY)

# ---------- SUMMARIZATION ----------
def summarize_gemini(text: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        return model.generate_content("Summarize this:\n" + text).text
    except Exception as e:
        return f"Gemini Error: {e}"

def summarize_groq(text: str):
    try:
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",  # free Groq model
            messages=[{"role": "user", "content": "Summarize this:\n" + text}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"

def compare_models(text: str):
    return {
        "gemini": summarize_gemini(text),
        "groq": summarize_groq(text)
    }

# ---------- EXTRA FEATURES ----------
def analyze_sentiment(text: str):
    return TextBlob(text).sentiment  # polarity (-1..1), subjectivity (0..1)

def detect_language(text: str):
    return detect(text)

def estimate_cost(text: str, model: str = "gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model)
    tokens = tokenizer.encode(text)
    usage = len(tokens)
    return {"tokens": usage, "cost_usd": usage/1000 * 0.002}  # approx only
