from wsgiref import headers

import requests


def get_requests(url):
    response = requests.get(url)
    if response.headers['Content-Type'] == 'application/json':
        return response.json()
    if response.headers['Content-Type'] == 'text/html':
        return response.text


def post_requests(url, data=None):
    reponse = requests.post(url=url, data=data)
    return reponse.json()
