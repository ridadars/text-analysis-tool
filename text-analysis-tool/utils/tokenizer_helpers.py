# utils/tokenizer_helpers.py
from transformers import AutoTokenizer
import matplotlib.pyplot as plt

def tokenize_text(text: str, model: str = "bert-base-uncased"):
    tokenizer = AutoTokenizer.from_pretrained(model)
    tokens = tokenizer.tokenize(text)
    ids = tokenizer.convert_tokens_to_ids(tokens)
    return {
        "tokens": tokens,
        "ids": ids,
        "length": len(tokens)
    }

def plot_token_lengths(texts, model: str = "bert-base-uncased"):
    tokenizer = AutoTokenizer.from_pretrained(model)
    lengths = [len(tokenizer.tokenize(t)) for t in texts]
    plt.hist(lengths, bins=10)
    plt.title(f"Token Distribution ({model})")
    plt.show()
