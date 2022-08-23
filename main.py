import requests
import csv


def get_data(page):
    url = 'https://storify.me/json'
    options = {
        'method': 'getlisting',
        'page': page,
        'sort': ''
    }
    response = requests.post(url, options)
    result = response.json()['result']['data']
    article_list = []
    for data in result:
        social_name = data['social_name']
        tag_list = []
        tags = data['tag']
        for tag in tags:
            tag_list.append(tag['name'])
        name = data['data']['name']
        description = ''
        followers = ''
        try:
            description = data['data']['biography']
        except:
            description = data['data']['signature']
        try:
            followers = data['data']['follows_by_count']
        except:
            followers = data['data']['followercount']
        profile_url = f'https://storify.me/ig/{social_name}'
        article_list.append({
            'Name': social_name,
            'URL': profile_url,
            'Followers': followers,
            'Category': tag_list,
            'Description': description,
        })
    return article_list


def save():
    with open('Beyond.csv', "a", newline="") as file:
        columns = ['Name', 'URL', 'Followers', 'Category', 'Description']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for x in range(1, 252):
            print('Parsing ', x, ' page')
            writer.writerows(get_data(x))


save()
