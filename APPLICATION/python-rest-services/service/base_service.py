from flask import Flask
from flask_restful import Resource

app = Flask(__name__)


class BaseServices(Resource):
    def __init__(self):
        print('base service constructor')
