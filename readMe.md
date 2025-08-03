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

2. Frontend
bash
Copy
Edit
cd dashboard
pip install streamlit requests
streamlit run dashboard.py

------------------------------------------------------------------------------------------

 #################_____Social Media Sentiment Analysis Dashboard: What Is It and How Does It Work?__________##############
What is it?
This project is a mini data platform that lets users instantly analyze the sentiment (positive/negative/neutral) of social media posts about any topic, through a simple web dashboard. It simulates real-time social listening for brands, news, or trends.

How does it work?
1. Web API Backend (FastAPI, HuggingFace Transformers)
You enter a topic or hashtag (e.g., “AI”, “Python”, “Palantir”) into the dashboard.

The FastAPI backend generates sample tweets about that topic (or, in a full version, fetches real tweets using Twitter API).

For each “tweet,” the backend uses a state-of-the-art sentiment analysis model (DistilBERT from HuggingFace) to predict if it’s positive, negative, or neutral.

2. Live Dashboard (Streamlit)
The Streamlit frontend connects to the backend.

You type a topic and click “Analyze.”

Instantly, you see a list of tweets with their predicted sentiment—easy to scan, no coding needed.

What’s the real-world value?
Brand Monitoring: Companies can track what people are saying about them in real-time.

Market Research: See if people like or dislike new products, policies, or events.

Trend Detection: Understand the mood of a crowd or social network about anything.

Why is it a good engineering project?
APIs: Combines REST API (FastAPI) with a modern ML model.

ML Deployment: Uses real, production-ready NLP (Natural Language Processing) for inference, not just training.

Full Stack: Shows ability to build both backend logic and frontend visualization.

Extensible: Can easily upgrade to fetch real data (from Twitter) or analyze large-scale sentiment in batch mode.

Stack Recap
Backend: FastAPI (Python), HuggingFace Transformers (DistilBERT)

Frontend: Streamlit (Python)

(Future): Tweepy for real Twitter data

In short:
You built a cloud-style app that lets anyone check public mood on any topic in real time, using advanced AI