from flask import request
from service.base_service import BaseServices


class DataService(BaseServices):

    def __init__(self):
        print('DataService constructor ')

    def get(self, id):
        print('get() execution ')
        return {'messageId': 'welcome to espark for id ' + id}

    def put(self, id):
        print('put() execution ')
        request_payload = request.get_json()
        return {'messageId': 'welcome to espark for id ' + id, 'payload': request_payload}

    def post(self):
        print('post() execution ')
        request_payload = request.get_json()
        return {'requestPayload': request_payload}, 201

    def delete(self, id):
        print('delete() execution ')
        return {'messageId': 'welcome to espark for id ' + id}



