import requests


def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'YourApp/1.0'}

    # Make a GET request to the Reddit API to get the hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for i, post in enumerate(posts):
                title = post['data']['title']
                print(f'{i + 1}. {title}')
        else:
            print('No posts found.')
    else:
        # Invalid subreddit or other error
        print('None')


# Example usage:
subreddit_name = 'learnpython'
print(f'Top 10 posts in r/{subreddit_name}:')
top_ten(subreddit_name)
