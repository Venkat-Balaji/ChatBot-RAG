import tweepy
import os

# Setup Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

def authenticate_twitter():
    # Authenticate with the Twitter API
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def retrieve_context(user_input, data_source):
    if data_source == "Twitter":
        api = authenticate_twitter()
        
        # Search for tweets related to the user input
        try:
            tweets = api.search_tweets(q=user_input, count=5, lang="en")
            context = [tweet.text for tweet in tweets]
            
            # Log context for debugging
            print("Retrieved Tweets: ", context)
            
            if not context:
                return "No relevant tweets found."
            
            return " ".join(context)  # Join tweets into a single string context

        except tweepy.TweepError as e:
            print(f"Error fetching tweets: {e}")
            return "Error retrieving data from Twitter."
    
    elif data_source == "NewsAPI":
        # Implement news context retrieval logic
        pass

    return []
