import datetime
import random
import textwrap
import requests

def fetch_dummy_sentiment_data():
    # Симуляция анализа с разных источников (в реальной версии сюда можно подключить API)
    sources = ['Twitter', 'Reddit', 'CryptoNews']
    data = {}
    for source in sources:
        score = random.uniform(-1, 1)  # от -1 (страх) до 1 (жадность)
        data[source] = score
    return data

def calculate_fear_greed_index(sentiment_scores):
    combined_score = sum(sentiment_scores.values()) / len(sentiment_scores)
    return round((combined_score + 1) * 50)  # от 0 до 100

def display_ascii_gauge(index):
    blocks = int(index / 5)
    bar = "█" * blocks + "-" * (20 - blocks)
    status = ""
    if index < 25:
        status = "😱 Extreme Fear"
    elif index < 50:
        status = "😟 Fear"
    elif index < 75:
        status = "😄 Greed"
    else:
        status = "🚀 Extreme Greed"
    print(f"\n[Crypto Sentiment Index]\n\n[{bar}] {index}/100  {status}\n")

def main():
    print(f"🧠 Analyzing crypto sentiment... ({datetime.datetime.now().isoformat()})")
    sentiment_data = fetch_dummy_sentiment_data()
    for src, val in sentiment_data.items():
        print(f" - {src}: {'{:+.2f}'.format(val)}")

    index = calculate_fear_greed_index(sentiment_data)
    display_ascii_gauge(index)

if __name__ == "__main__":
    main()
