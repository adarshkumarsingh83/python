from src.exception.application_exception import ApplicationException
from flask import Flask, request, json, Response
from flask_restful import Resource
import logging as log
import json

app = Flask(__name__)

file_config = {
    "name": "db.json"
}


class AppConfig:

    def __init__(self):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        log.info('AppConfig Constructor ')
        self.data = {}

    def get_file_data(self):
        try:
            with open(file_config.get('name'), 'r') as json_file:
                json_data = json.load(json_file)
                return json_data
        except Exception as e:
            raise ApplicationException({"fetch-status": "failed"})

    def put_file_data(self, data):
        try:
            with open(file_config.get('name'), 'w') as json_file:
                json_file.write(json.dumps(data))
                json_file.close()
                return {"status": "success", "data": data}
        except Exception as e:
            raise ApplicationException({"saved-status": "failed"})

    def add_data(self, data):
        try:
            user_data = self.get_file_data()
            user_data.append(data)
            return self.put_file_data(user_data)
        except Exception as e:
            raise ApplicationException({"saved-status": "failed"})

    def get_data(self, id):
        try:
            user_data = self.get_file_data()
            for user in user_data:
                if user.get('id') == int(id):
                    return {"fetch-status": "user fetched", "data": user}
                else:
                    continue
            return {"fetch-status": "user not found"}
        except Exception as e:
            raise ApplicationException({"fetch-status": "failed"})

    def update_data(self, id, user_update):
        try:
            user_data = self.get_file_data()
            for index, user in enumerate(user_data):
                if user.get('id') == int(id):
                    user_data[index] = user_update
                    self.put_file_data(user_data)
                    return {"update-status": "user updated", "data": user_update}
                else:
                    continue

            return {"update-status": "user not found for update "}
        except Exception as e:
            raise ApplicationException({"update-status": "failed"})

    def delete_data(self, id):
        try:
            user_data = self.get_file_data()
            for index, user in enumerate(user_data):
                if user.get('id') == int(id):
                    del user_data[index]
                    self.put_file_data(user_data)
                    return {"delete-status": "user deleted ", "data": user}
                else:
                    continue

            return {"update-status": "user not found for update "}
        except Exception as e:
            raise ApplicationException({"update-status": "failed"})

    def check_empty_file(self):
        try:
            data = self.get_file_data();
            if data == '':
                return True
            else:
                return False
        except Exception as e:
            return True
