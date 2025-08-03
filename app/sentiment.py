from transformers import pipeline

# Load a sentiment-analysis pipeline (one time on startup)
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    return sentiment_pipeline(text)[0]["label"]
