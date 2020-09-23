from flask import Flask
from flask_restful import Resource, Api

app_greet = Flask(__name__)
api_greet = Api(app_greet)


class GreetWorld(Resource):

    def get(self):
        return {'messagge': 'welcome to espark'}


api_greet.add_resource(GreetWorld, '/')
