from src.config.app_config import *
from src.services.user_service import *

user_service = UserService()


class UserController:
    def __init__(self):
        log.info('UserController constructor')


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    log.info('UserController get() execution ')
    try:
        user_service.abort_if_user_doesnt_exist(id)
        user = user_service.get_user_by_id(id)
        return Response(response=json.dumps({'user-fetched-status': user}),
                        status=200,
                        mimetype='application/json')
    except ValidationError as e:
        return Response(response=json.dumps({'user-fetched-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/user/<id>', methods=['PUT'])
def put_user(id):
    log.info('UserController put() execution ')
    try:
        user_service.abort_if_user_doesnt_exist(id)
        request_payload = request.get_json()
        status = user_service.update_user(id, request_payload)
        return Response(response=json.dumps({'user-updated-status': status}),
                        status=201,
                        mimetype='application/json')
    except ValidationError as e:
        return Response(response=json.dumps({'user-updated-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/user', methods=['POST'])
def post_user():
    log.info('UserController post() execution ')
    request_payload = request.get_json()
    response = user_service.create_user(request_payload)
    return Response(response=json.dumps({'user-saved-status': response}),
                    status=201,
                    mimetype='application/json')


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    log.info('UserController delete() execution ')
    try:
        user_service.abort_if_user_doesnt_exist(id)
        response = user_service.delete_user_by_id(id)
        return Response(response=json.dumps({'user-deleted-status': response}),
                        status=200,
                        mimetype='application/json')
    except ValidationError as e:
        return Response(response=json.dumps({'user-deleted-status': e.message}),
                        status=404,
                        mimetype='application/json')


@app.route('/users', methods=['GET'])
def get_all_users():
    log.info('UserController get() execution ')
    users = user_service.get_users()
    return Response(response=json.dumps({'users-fetched-status': users}),
                    status=200,
                    mimetype='application/json')
