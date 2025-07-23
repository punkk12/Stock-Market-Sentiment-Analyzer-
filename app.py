from flask import Flask, jsonify
from sentiment_analyzer.fetch_news import fetch_sample_news
from sentiment_analyzer.sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route("/sentiment")
def sentiment():
    headlines = fetch_sample_news()
    results = [{"headline": h, "sentiment": analyze_sentiment(h)} for h in headlines]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
