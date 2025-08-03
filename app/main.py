from fastapi import FastAPI, Query
from .sentiment import get_sentiment

app = FastAPI()

@app.get("/sentiment")
def sentiment(topic: str = Query(...)):
    # --- Replace this block with real tweets in the future! ---
    tweets = [
        f"{topic} is awesome!",
        f"I dislike {topic}.",
        f"{topic} is okay, could be better.",
        f"Absolutely love {topic}!",
        f"Not a fan of {topic} right now."
    ]
    # ----------------------------------------------------------
    results = [{"tweet": t, "sentiment": get_sentiment(t)} for t in tweets]
    return {"results": results}
