from flask_restful import abort
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
        self.client = MongoClient("mongodb://localhost:27017/")
        database = MongoDb.data['database']
        collection = MongoDb.data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = MongoDb.data
        self.init_db()

    def init_db(self):
        log.info('MongoDb init_db() ')
        if self.collection.find({'_id': 1}) == '':
            for k, v in USERS.items():
                x = self.collection.insert_one({'_id': k, 'data': v})
                print(x.inserted_id)

    def get_users(self):
        log.info('MongoDb get_users() ')
        users = self.collection.find()
        return [{item: data[item] for item in data} for data in users]

    def update_user(self, id, user):
        log.info('MongoDb update_user() ')
        response = self.collection.update_one({'_id': id}, {"$set": user})
        return {'Status': 'Successfully Updated' if response.modified_count > 0 else "Updated UnSuccessful"}

    def create_user(self, user):
        log.info('MongoDb create_user() ')
        return self.collection.insert(user)

    def get_user_by_id(self, id):
        log.info('MongoDb get_user_by_id() ')
        user = self.collection.find({'_id': id})
        return [{item: data[item] for item in data} for data in user]

    def delete_user_by_id(self, id):
        log.info('MongoDb delete_user_by_id() ')
        response = self.collection.delete_one({'_id': id})
        return {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Deleted UnSuccessful"}

    def abort_if_user_doesnt_exist(self, id):
        log.info('MongoDb abort_if_user_doesnt_exist() ')
        if self.collection.find({'_id': id}) == '':
            abort(404, message="User {} doesn't exist".format(id))
