from flask import request
from web.abstract_controller import AbstractController
from services.user_service import abort_if_user_doesnt_exist, USERS


class UserController(AbstractController):

    def __init__(self):
        print('UserController Constructor ')

    def get(self):
        print('get() execution ')
        return {'users-fetched': USERS}, 200

    def get(self, id):
        print('get() execution ')
        abort_if_user_doesnt_exist(id)
        return {'user-fetched': USERS[id]}, 200

    def put(self, id):
        print('put() execution ')
        abort_if_user_doesnt_exist(id)
        request_payload = request.get_json()
        USERS[id] = request_payload
        return {'user-updated': request_payload}, 201

    def post(self):
        print('post() execution ')
        request_payload = request.get_json()
        id = int(max(USERS.keys())) + 1
        USERS[id] = request_payload
        return {'user-saved': request_payload}, 201

    def delete(self, id):
        print('delete() execution ')
        abort_if_user_doesnt_exist(id)
        user = USERS[id]
        del USERS[id]
        return {'user-deleted': user}, 204


class UserControllerList(AbstractController):
    def __init__(self):
        print('UserController Constructor ')

    def get(self):
        print('get() execution ')
        return {'users-fetched': USERS}, 200
