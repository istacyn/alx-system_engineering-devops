#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
