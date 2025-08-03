import streamlit as st
import requests

st.title("Social Media Sentiment Analysis")

topic = st.text_input("Enter a topic or hashtag", "AI")

if st.button("Analyze"):
    r = requests.get("http://localhost:8000/sentiment", params={"topic": topic})
    results = r.json()["results"]
    st.write(f"Showing results for: {topic}")
    for row in results:
        st.write(f"**{row['tweet']}**  —  *{row['sentiment']}*")
