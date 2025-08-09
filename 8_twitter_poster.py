#!/usr/bin/env python3
"""
Twitter Poster - Post tweets using Twitter API
"""

import tweepy
import getpass

def post_tweet():
    """Post a tweet using Twitter API"""
    print("=== Twitter Poster ===")
    print("Note: You need Twitter API credentials to use this service.")
    print("Get them from: https://developer.twitter.com/")
    
    api_key = input("Enter your API Key: ")
    api_secret = getpass.getpass("Enter your API Secret (hidden): ")
    access_token = input("Enter your Access Token: ")
    access_secret = getpass.getpass("Enter your Access Token Secret (hidden): ")
    
    tweet_text = input("Enter your tweet (max 280 characters): ")
    
    if len(tweet_text) > 280:
        print("⚠️ Warning: Tweet is longer than 280 characters. It will be truncated.")
        tweet_text = tweet_text[:280]
    
    try:
        # Authenticate
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        api = tweepy.API(auth)
        
        # Verify credentials
        api.verify_credentials()
        print("✅ Authentication successful!")
        
        # Post tweet
        api.update_status(tweet_text)
        print("✅ Tweet posted successfully!")
        print(f"Tweet content: {tweet_text}")
        
    except Exception as e:
        print(f"❌ Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet() 