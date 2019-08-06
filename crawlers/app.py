import requests

subreddit = 'GlobalOffensive'
url = 'https://old.reddit.com/r/'

page = requests.get(url + subreddit, headers = {'User-agent': 'python-crawler:1.0.0'})

print(page.text)

print('yeah this is working fine')