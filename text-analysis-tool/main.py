# main.py
import gradio as gr
from utils.llm_helpers import compare_models, analyze_sentiment, detect_language, estimate_cost
from utils.tokenizer_helpers import tokenize_text

def analyze(text):
    summaries = compare_models(text)
    tokens = tokenize_text(text)
    sentiment = analyze_sentiment(text)
    lang = detect_language(text)
    cost = estimate_cost(text)
    return summaries, tokens, sentiment, lang, cost

iface = gr.Interface(
    fn=analyze,
    inputs="text",
    outputs=["json", "json", "json", "text", "json"],
    title="LLM Text Analysis Tool (Gemini + Groq)"
)

if __name__ == "__main__":
    iface.launch()
