# news_api.py
import requests

# NewsAPI credentials
NEWSAPI_KEY = "39f1979388ee40c68153808b12aa8740"

def fetch_news(query, count=5):
    """Fetch news articles related to the query."""
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWSAPI_KEY}&pageSize={count}"
    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])
        return [article["title"] + ": " + article["description"] for article in articles]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
