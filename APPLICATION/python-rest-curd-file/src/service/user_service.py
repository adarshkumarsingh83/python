from flask_restful import abort
from src.exception.validation_exception import ValidationException
from src.config.application_config import *

users_list = [
    {'id': 1, 'name': 'adarsh kumar'},
    {'id': 2, 'name': 'radha singh'},
    {'id': 3, 'name': 'amit kumar'}
]


class UserService:

    def __init__(self):
        log.info('UserService constructor')
        self.config = AppConfig()
        self.init_db()

    def init_db(self):
        log.info('AppConfig init_db() ')
        if self.config.check_empty_file():
            self.config.put_file_data(users_list)
        else:
            log.info('user db file has data ')

    def get_users(self):
        log.info('UserService get_users() ')
        try:
            user = self.config.get_file_data()
            return {'id': "id", 'name': user}
        except Exception as e:
            return {'status': 'failed to fetch users'}

    def update_user(self, id, user):
        log.info('UserService update_user() ')
        try:
            return self.config.update_data(id, user)
        except Exception as e:
            return {'status': 'failed', 'data': ""}

    def create_user(self, user):
        log.info('UserService create_user() ')
        try:
            return self.config.add_data(user)
        except Exception as e:
            return {'status': 'failed', 'data': user}

    def get_user_by_id(self, id):
        log.info('UserService get_user_by_id() ')
        try:
            return self.config.get_data(id)
        except Exception as e:
            return {'status': 'failed to fetched user', 'id': "id"}

    def delete_user_by_id(self, id):
        log.info('UserService delete_user_by_id() ')
        try:
            return self.config.delete_data(id)
        except Exception as e:
            return {'status': 'failed to delete user', 'id': "id"}

    def abort_if_user_doesnt_exist(self, id):
        log.info('UserService abort_if_user_doesnt_exist() ')
        user = self.config.get_data(id)
        if user == '':
            return False
        else:
            return True
