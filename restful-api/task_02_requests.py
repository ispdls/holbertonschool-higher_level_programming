import requests
import json
import csv

"""Create a function fetch_and_print_posts() 
that fetches all post from JSONPlaceholder."""


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {r.status_code}')
    if r.ok:
        
        datas = r.json()

        for data in datas:
            print(data['title'])


"""Create a function fetch_and_save_posts() 
that fetches all post from JSONPlaceholder."""


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = r.json()
    if r.ok:
      
        dict_post = []

        for post in posts:
           
            post_data = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }

            dict_post.append(post_data)

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:

            fieldnames = ['id', 'title', 'body']

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(dict_post)

fetch_and_print_posts()