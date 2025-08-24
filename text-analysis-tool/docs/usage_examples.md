# Usage Examples

## Example 1: Summarization
**Input:** A news article from `data/sample_texts/news.txt`  
**Output:**  
- Gemini: "UN announces urgent climate action with focus on renewable energy."  
- Groq: "Global carbon emissions must drop 45% before 2030, but enforcement remains weak."

---

## Example 2: Sentiment Analysis
**Input:** "I love this product, but delivery was slow."  
**Output:** `Sentiment(polarity=0.3, subjectivity=0.6)`

---

## Example 3: Language Detection
**Input:** "یہ ایک اچھا دن ہے"  
**Output:** `"ur"`

---

## Example 4: Tokenization
**Input:** "Transformers are powerful models."  
**Output:**  
```json
{
  "tokens": ["transformers", "are", "powerful", "models"],
  "ids": [19081, 2024, 3928, 4829],
  "length": 4
}
