from wsgiref import headers

import requests


def get_requests(url):
    response = requests.get(url)
    if url == 'http://127.0.0.1:18980/data/':
        response_result = response.json()
    if url == 'http://127.0.0.1:18980/data/html':
        response_result = response.text
    return response_result


# def post_requests(positionName, headers):
#     url = 'http://127.0.0.1:18980/data/position'
#     payload = {
#         "firstType": "市场|商务类",
#         "positionType": "市场|营销",
#         "positionThirdType": "市场营销",
#         "positionName": positionName,
#         "workAddress": "北京市海淀区时代网络大厦4层"
#     }
#     if headers.get('Content-Type') == 'text/plain':
#         reponse = requests.post(url = url, data = payload, headers = headers)
#         return reponse.json()
#     if headers.get('Content-Type') == 'application/x-www-form-urlencoded':
#         reponse = requests.post(url = url, data = payload, headers = headers)
#         return reponse.json()

def post_requests(positionName):
    url = 'http://127.0.0.1:18980/data/position'
    payload = {
            "firstType": "市场|商务类",
            "positionType": "市场|营销",
            "positionThirdType": "市场营销",
            "positionName": positionName,
            "workAddress": "北京市海淀区时代网络大厦4层"
        }
    reponse = requests.post(url=url, data=payload)
    return reponse.json()


# if __name__ == '__main__':
#     r = post_requests("职位名称")
#     print(r)


