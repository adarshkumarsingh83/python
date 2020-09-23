from flask import Flask
from flask_restful import Resource

app = Flask(__name__)


class AbstractController(Resource):
    def __init__(self):
        print('AbstractController Constructor')

