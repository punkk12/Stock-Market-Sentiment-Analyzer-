def print_sentiment_scores(news_list, analyzer_func):
    for news in news_list:
        score = analyzer_func(news)
        print(f"News: {news}")
        print(f"Sentiment: {score}\n")
