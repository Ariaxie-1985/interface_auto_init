from data import data
from data.get_index import get_Index
from data.post_json_form import post_Json
from flask_restful import Api
api = Api(data)
api.add_resource(get_Index, '/html')
api.add_resource(post_Json, '/position')

