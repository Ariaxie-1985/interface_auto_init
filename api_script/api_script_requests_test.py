from utils.util import get_requests, post_requests


def data_api():
    url = 'http://127.0.0.1:18980/data/'
    return get_requests(url)


def html_api():
    url = 'http://127.0.0.1:18980/data/html'
    return get_requests(url)


def position_api():
    url = 'http://127.0.0.1:18980/data/position'
    data = {
        "firstType": "市场|商务类",
        "positionType": "市场|营销",
        "positionThirdType": "市场营销",
        "positionName": "高级市场营销经理",
        "workAddress": "北京市海淀区时代网络大厦4层"
    }
    return post_requests(url=url, data=data)
