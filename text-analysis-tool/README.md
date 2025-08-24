# Text Analysis Tool (Buildables AI Fellowship)

## 📌 Overview
This project is a Text Analysis Tool that demonstrates LLM basics, tokenization, and API usage.  
It compares summaries from **Gemini** and **Groq** APIs, while also providing:
- Tokenization analysis
- Sentiment analysis
- Language detection
- Token usage & cost estimation

## 🚀 Features
- Text summarization (Gemini + Groq)
- Multi-model comparison
- Token statistics
- Sentiment analysis
- Language detection
- Cost estimation

## 📂 Project Structure
text-analysis-tool/
│── main.py
│── config.py
│── requirements.txt
│── README.md
│
├── utils/
│ ├── llm_helpers.py
│ ├── tokenizer_helpers.py
│ └── init.py
│
├── data/
│ ├── sample_texts/
│ └── results/
│
├── docs/
│ └── usage_examples.md
│
└── tests/
└── test_main.py