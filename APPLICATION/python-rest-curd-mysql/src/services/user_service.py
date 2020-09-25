from flask_restful import abort
from src.exception.validation_exception import ValidationError
from src.config.app_config import *

users_list = [
    {'id': 1, 'name': 'adarsh kumar'},
    {'id': 2, 'name': 'radha singh'},
    {'id': 3, 'name': 'amit kumar'}
]


class UserService:

    def __init__(self):
        log.info('UserService constructor')
        self.init_db()

    def init_db(self):
        log.info('AppConfig init_db() ')
        if self.empty_check() != 1:
            for dic in users_list:
                id_value = dic.get('id')
                name_value = dic.get('name')
                val = (id_value, name_value)
                my_cursor.execute(insert_sql, val)

            mydb.commit()
        else:
            log.info('user table has data ')

    def empty_check(self):
        my_cursor.execute(empty_check_sql)
        response = my_cursor.fetchone()
        return response[0]

    def get_users(self):
        log.info('UserService get_users() ')
        try:
            my_cursor.execute(select_all_sql)
            users = my_cursor.fetchall()
            return users
        except Exception as e:
            return {'status': 'failed to fetch users'}

    def update_user(self, id, user):
        log.info('UserService update_user() ')
        try:
            name_val = user.get('name')
            update_sql_copy = update_sql.replace("$id", id)
            update_sql_copy = update_sql_copy.replace("$name", name_val)
            my_cursor.execute(update_sql_copy)
            mydb.commit()
            return {'id': id, 'name': name_val}
        except Exception as e:
            return {'status': 'failed', 'data': user}

    def create_user(self, user):
        log.info('UserService create_user() ')
        try:
            id_val = user.get('id')
            name_val = user.get('name')
            my_cursor.execute(insert_sql, (id_val, name_val))
            mydb.commit()
            return {'id': id_val, 'name': name_val}
        except Exception as e:
            return {'status': 'failed', 'data': user}

    def get_user_by_id(self, id):
        log.info('UserService get_user_by_id() ')
        try:
            my_cursor.execute(select_by_id_sql.replace("$id", id))
            user = my_cursor.fetchone()
            return {'id': user[0], 'name': user[1]}
        except Exception as e:
            return {'status': 'failed to fetched user', 'id': id}

    def delete_user_by_id(self, id):
        log.info('UserService delete_user_by_id() ')
        try:
            my_cursor.execute(select_by_id_sql.replace("$id", id))
            user = my_cursor.fetchone()
            user = {'id': user[0], 'name': user[1]}
            my_cursor.execute(delete_sql.replace("$id", id))
            mydb.commit()
            if my_cursor.rowcount == 1:
                return user
            else:
                return {'status': 'failed to delete user', 'id': id}
        except Exception as e:
            return {'status': 'failed to delete user', 'id': id}

    def abort_if_user_doesnt_exist(self, id):
        log.info('UserService abort_if_user_doesnt_exist() ')
        my_cursor.execute(select_by_id_sql.replace("$id", id))
        user = my_cursor.fetchone()
        if user is None:
            raise ValidationError("User {} doesn't exist".format(id))
