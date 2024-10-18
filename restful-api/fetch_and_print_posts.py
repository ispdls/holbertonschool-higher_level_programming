import requests
import json

"""Create a function fetch_and_print_posts() 
that fetches all post from JSONPlaceholder."""


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r)
    if r.ok:
        datas = r.json()

        for data in datas:
            print(data['title'])

fetch_and_print_posts()
