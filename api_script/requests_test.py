from utils.util import get_requests, post_requests


def data_api():
    url = 'http://127.0.0.1:18980/data/'
    return get_requests(url)


def html_api():
    url = 'http://127.0.0.1:18980/data/html'
    return get_requests(url)

def position_api():
    position_name = "接口传入职位名称"
    return post_requests(position_name)


# def pisition_json_api():
#     position_name = "接口传入的职位名称"
#     header_type = {'Content-Type':'text/plain'}
#     #return post_requests(position_name, header_type)
#     print(post_requests(position_name, header_type))
#
# def pisition_form_api():
#     position_name = "接口传入的职位名称"
#     header_type = {'Content-Type': 'application/x-www-form-urlencoded'}
#     return post_requests(position_name, header_type)

# if __name__ == '__main__':
#     r = position_api()
#     print(r)