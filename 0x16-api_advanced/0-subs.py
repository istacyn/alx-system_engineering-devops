#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API to retrieve number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: The number of subscribers for the subreddit.
        0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    return 0
