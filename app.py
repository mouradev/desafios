import requests
from bs4 import BeautifulSoup

subreddit = 'cats'
url = 'https://old.reddit.com/r/'

thread_count = 0

raw_page = requests.get(url + subreddit, headers = {'User-agent': 'python-crawler:1.0.0'})

soup = BeautifulSoup(raw_page.text, 'html.parser')

# print(soup.prettify())
threads = soup.find_all(class_='thing')

for thread in threads:
    thread_count += 1

    score = int(thread.get('data-score'))
    if(score >= 5000):
        # print(thread.attrs)
        title = thread.find('a', class_='title').get_text()
        line = str(score) + ' - ' + title
        print(line)
    
        
last_id = thread.get('id').split('thing_t3_')[1]
print('last id: ' + last_id)