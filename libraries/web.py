# Python HTTP requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

if response.status_code == 200:
    titles = [post['title'] for post in posts]
    for i, title in enumerate(titles, start=1):
        print(f"{i}: {title}")
else:
    print('Error getting response')
