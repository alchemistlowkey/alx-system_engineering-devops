#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    '''Returns the number of subscribers'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return subscribers_count
    else:
        return 0
