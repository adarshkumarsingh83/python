from src.exception.validation_exception import ValidationException
from src.exception.application_exception import ApplicationException
from pymongo import MongoClient
import logging as log

USERS = {
    '1': {'name': 'adarsh kumar'},
    '2': {'name': 'radha singh'},
    '3': {'name': 'amit kumar'},
}


class MongoDb:
    data = {
        "database": "espark-db",
        "collection": "users",
    }

    def __init__(self):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            database = MongoDb.data['database']
            collection = MongoDb.data['collection']
            cursor = self.client[database]
            self.collection = cursor[collection]
            self.data = MongoDb.data
            self.init_db()
        except Exception as e:
            log.error(e)

    def init_db(self):
        log.info('MongoDb init_db() ')
        try:

            if self.check_db_empty():
                for k, v in USERS.items():
                    x = self.collection.insert_one({'_id': k, 'data': v})
                    print(x.inserted_id)

        except Exception as e:
            log.error('exception in init_db')

    def get_users(self):
        log.info('MongoDb get_users() ')
        user_list = []
        try:
            response = self.collection.find()
            for x in response:
                user_list.append(x)
            return user_list
        except Exception as e:
            raise ApplicationException("User data not found in db")

    def update_user(self, id, user):
        log.info('MongoDb update_user() ')
        try:
            response = self.collection.update_one({'_id': id}, {"$set": user})
            return {'Status': 'Successfully Updated' if response.modified_count > 0 else "Updated UnSuccessful"}
        except Exception as e:
            raise ApplicationException("User not updated in db")

    def create_user(self, user):
        log.info('MongoDb create_user() ')
        try:
            return self.collection.insert(user)
        except Exception as e:
            raise ApplicationException("User not created in db")

    def get_user_by_id(self, id):
        log.info('MongoDb get_user_by_id() ')
        try:
            user = self.collection.find({'_id': id})
            return [{item: data[item] for item in data} for data in user]
        except Exception as e:
            raise ApplicationException("User not found in db")

    def delete_user_by_id(self, id):
        log.info('MongoDb delete_user_by_id() ')
        try:
            response = self.collection.delete_one({'_id': id})
            return {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Deleted UnSuccessful"}
        except Exception as e:
            raise ApplicationException("User not delete in db")

    def abort_if_user_doesnt_exist(self, id):
        log.info('MongoDb abort_if_user_doesnt_exist() ')
        if self.collection.find({'_id': id}) == '':
            raise ValidationException("User {} doesn't exist".format(id))

    def check_db_empty(self):
        var = self.collection.find()
        for element in var:
            if element.get('_id') == '':
                return True
            else:
                return False
        return True
