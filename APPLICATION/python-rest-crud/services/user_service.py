from flask_restful import abort

USERS = {
    '1': {'name': 'adarsh kumar'},
    '2': {'name': 'radha singh'},
    '3': {'name': 'amit kumar'},
}


def abort_if_user_doesnt_exist(id):
    var: bool = check_key(USERS, id)
    if var is False:
        abort(404, message="User {} doesn't exist".format(id))


def check_key(users, key):
    for k, v in users.items():
        if k != int(key):
            continue
        else:
            return True
    return False
