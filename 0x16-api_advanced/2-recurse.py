#!/usr/bin/python3
"""
Queries the Reddit API and returns a list
containing the titles of all hot articles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve the titles
    of all hot articles for a given subreddit.

    Returns:
        list: A list containing the titles of all hot articles.
        None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        if not children:
            return hot_list

        for post in children:
            title = post["data"]["title"]
            hot_list.append(title)

        # Recursively call the function with the 'after' token for pagination
        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after)
    return None
