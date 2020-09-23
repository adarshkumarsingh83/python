from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app_data = Flask(__name__)
api_data = Api(app_data)

parser = reqparse.RequestParser()
parser.add_argument('id')


class DataService(Resource):

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


api_data.add_resource(DataService, '/data', endpoint='post')
api_data.add_resource(DataService, '/data/<id>', endpoint='get')
api_data.add_resource(DataService, '/data/<id>', endpoint='put')
api_data.add_resource(DataService, '/data/<id>', endpoint='delete')
