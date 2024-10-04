# twitter_api.py
import tweepy

# Twitter API credentials (replace these with your actual credentials)
API_KEY = "6gXbFhJ3E3DetOsdSS5obLOVq"
API_SECRET = "uHdBLaCeIR2MO4o7KSHiXTfCrMtGFAYLuDatwaN4oy4o5s5J16"
ACCESS_TOKEN = "1838605439233122304-WgQdkPW2XRk3y2c9H0y8PHWbkXnRd6"
ACCESS_SECRET = "pPrOBcR6mytytf4uH974DAFGVHtm39TE5RNAAfwokEBgD"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_tweets(query, count=5):
    """Fetch tweets related to the query."""
    try:
        tweets = api.search_tweets(q=query, count=count, lang="en", tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []
