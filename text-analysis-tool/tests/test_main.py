from utils.llm_helpers import summarize_gemini, analyze_sentiment, detect_language

def test_sentiment():
    text = "I love programming."
    result = analyze_sentiment(text)
    assert result.polarity > 0

def test_language():
    text = "Bonjour tout le monde"
    result = detect_language(text)
    assert result == "fr"

def test_gemini_summary():
    text = "AI is helping the world."
    result = summarize_gemini(text)
    assert isinstance(result, str)