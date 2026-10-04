import requests
import json
import pdb

# 1. The URL that provides the fake post data
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # 2. Fetch the data
    # pdb.set_trace()
    response = requests.get(url)
    response.raise_for_status() # Check for errors

    # 3. Parse the data
    # This specific URL returns a LIST of posts
    posts = response.json()

    print(f"Successfully fetched {len(posts)} posts.\n")

    # 4. Professional DevOps Logic: Only print the first 5 titles
    # We use a slice [:5] so we don't flood the terminal
    print("--- Latest 5 Post Titles ---")
    for post in posts[:5]:
        print(f"ID {post['id']}: {post['title']}")

except Exception as e:
    print(f"Failed to fetch posts: {e}")
