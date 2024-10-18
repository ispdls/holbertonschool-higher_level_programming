import requests
import json

"""Create a function fetch_and_print_posts() 
that fetches all post from JSONPlaceholder."""


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.ok:
        print(r)
        datas = r.json()

        for data in datas:
            print(data['title'])

fetch_and_print_posts()
