from flask import Flask, jsonify
import pandas as pd
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/api/tweets")
def get_tweets():
    try:
        df = pd.read_csv("data/tweets.csv")
    except FileNotFoundError:
        return jsonify({"error": "No tweets found. Run fetch_tweets.py first."})

    df["sentiment"] = df["content"].apply(analyze_sentiment)
    tweets = df.to_dict(orient="records")
    return jsonify(tweets)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
