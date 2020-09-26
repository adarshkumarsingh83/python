from flask import Flask, Response, json
from flask_restful import Resource
import logging as log

app = Flask(__name__)


class AbstractController(Resource):
    def __init__(self):
        print('AbstractController Constructor')
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')