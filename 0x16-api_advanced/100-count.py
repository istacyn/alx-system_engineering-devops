#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests
from collections import Counter

def count_words(subreddit, word_list, key_words={}, after=None, counts={}):
    """
    Recursively queries the Reddit API to count occurrences
    of keywords in hot article titles for a given subreddit.

    Returns:
        dict: A dictionary containing keyword counts.
        None if no results are found.
    """
    if not counts:
        key_words = {word.lower(): 0 for word in word_list}
        counts = Counter(word.lower()for word in word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for post in children:
            title = post["data"]["title"].lower()
            words = title.split()
            for word in key_words.keys():
                key_words[word] += words.count(word)

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, key_words, after, counts)
        else:
            for key in key_words.keys():
                key_words[key] *= counts[key]
            key_words = sorted(key_words.items(),
                               key=lambda item: (-item[1], item[0]))
            for item in key_words:
                if item[1] > 0:
                    print(f"{item[0]}: {item[1]}")
