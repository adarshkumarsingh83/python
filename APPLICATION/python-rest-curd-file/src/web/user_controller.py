from src.exception.validation_exception import ValidationException
from src.exception.application_exception import ApplicationException
from src.service.user_service import UserService
from flask import request, json, Response
from src.config.application_config import AppConfig, app, log


class UserController:
    def __init__(self):
        log.info('UserController constructor')


user_service = UserService()


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    log.info('UserController get() execution ')
    try:
        user_service.abort_if_user_doesnt_exist(id)
        user = user_service.get_user_by_id(id)
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
        user_service.abort_if_user_doesnt_exist(id)
        request_payload = request.get_json()
        status = user_service.update_user(id, request_payload)
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
        response = user_service.create_user(request_payload)
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
        user_service.abort_if_user_doesnt_exist(id)
        response = user_service.delete_user_by_id(id)
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
        users = user_service.get_users()
        return Response(response=json.dumps({'users-fetched': users}),
                        status=200,
                        mimetype='application/json')
    except ApplicationException as e:
        return Response(response=json.dumps({'users-fetched-status': e.message}),
                        status=200,
                        mimetype='application/json')
