#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Custom User-Agent header to avoid Too Many Requests error
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 302:
            # If the subreddit is invalid and redirects, return 0
            return 0
        else:
            print(f"Error: Failed to query subreddit. Status code: {response.status_code}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
