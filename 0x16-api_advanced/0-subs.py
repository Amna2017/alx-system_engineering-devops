import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'YourApp/1.0'}

    # Make a GET request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error
        return 0

# Example usage:
subreddit_name = 'learnpython'
subscribers = number_of_subscribers(subreddit_name)
if subscribers > 0:
    print(f'The subreddit r/{subreddit_name} has {subscribers} subscribers.')
else:
    print(f'The subreddit r/{subreddit_name} is not valid.')

