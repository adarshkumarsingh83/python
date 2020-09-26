from src.exception.validation_exception import ValidationException
from src.exception.application_exception import ApplicationException
from flask import request, json, Response
from src.web.abstract_controller import AbstractController, app, log
from src.services.user_service import MongoDb, USERS

mongoDb = MongoDb()


class UserController(AbstractController):
    def __init__(self):
        log.info('UserController constructor')


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    log.info('UserController get() execution ')
    try:
        mongoDb.abort_if_user_doesnt_exist(id)
        user = mongoDb.get_user_by_id(id)
        return Response(response=json.dumps({'user-fetched': user}),
                        status=200,
                        mimetype='application/json')
    except ValidationException as e:
        return Response(response=json.dumps({'user-fetched-status': e.message}),
                        status=404,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'user-updated-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/user/<id>', methods=['PUT'])
def put_user(id):
    log.info('UserController put() execution ')
    try:
        mongoDb.abort_if_user_doesnt_exist(id)
        request_payload = request.get_json()
        status = mongoDb.update_user(id, request_payload)
        return Response(response=json.dumps({'user-updated': status}),
                        status=201,
                        mimetype='application/json')
    except ValidationException as e:
        return Response(response=json.dumps({'user-updated-status': e.message}),
                        status=404,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'user-updated-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/user', methods=['POST'])
def post_user():
    log.info('UserController post() execution ')
    try:
        request_payload = request.get_json()
        response = mongoDb.create_user(request_payload)
        return Response(response=json.dumps({'user-saved': response}),
                        status=201,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'users-creation-status': e.message}),
                        status=500,
                        mimetype='application/json')


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    log.info('UserController delete() execution ')
    try:
        mongoDb.abort_if_user_doesnt_exist(id)
        response = mongoDb.delete_user_by_id(id)
        return Response(response=json.dumps({'user-deleted': response}),
                        status=200,
                        mimetype='application/json')
    except ValidationException as e:
        return Response(response=json.dumps({'user-deleted-status': e.message}),
                        status=404,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'user-updated-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/users', methods=['GET'])
def get_all_users():
    log.info('UserController get() execution ')
    try:
        users = mongoDb.get_users()
        return Response(response=json.dumps({'users-fetched': users}),
                        status=200,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'users-fetched-status': e.message}),
                        status=200,
                        mimetype='application/json')
