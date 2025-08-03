# Social Media Sentiment Analysis Dashboard

A FastAPI + Streamlit app for real-time sentiment analysis on social media topics using HuggingFace Transformers.

## Features
- Enter any topic or hashtag and get sentiment on related sample tweets
- Instant results with a simple web UI
- Easily extend to real Twitter API data (see roadmap)

## How to Run

### 1. Backend
```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
