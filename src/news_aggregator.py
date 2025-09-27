import requests

COINS = ["bitcoin", "ethereum"]

def fetch_news():
    print("Fetching crypto news (demo)...")
    # Demo static news
    news = [
        {"title": "Bitcoin hits new high!", "source": "CryptoTimes"},
        {"title": "Ethereum 2.0 launch update", "source": "BlockNews"},
    ]
    for item in news:
        print(f"{item['title']} - {item['source']}")

if __name__ == "__main__":
    fetch_news()
