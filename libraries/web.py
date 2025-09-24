# Python HTTP requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

if response.status_code == 200:
    titles = [post['title'] for post in posts]
    for title in titles:
        print(title)
else:
    print('Error getting response')
