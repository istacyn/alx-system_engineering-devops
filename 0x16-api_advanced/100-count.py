#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API to count occurrences
    of keywords in hot article titles for a given subreddit.

    Returns:
        dict: A dictionary containing keyword counts.
        None if no results are found.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        if not children:
            return counts

        for post in children:
            title = post["data"]["title"].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    counts[word.lower()] += 1

        after = data["data"]["after"]
        return count_words(subreddit, word_list, after, counts)
    return None
