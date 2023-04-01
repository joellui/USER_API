from pymongo import MongoClient
from bson.objectid import ObjectId
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['userDB']
users = db['users']

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        user = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        user_id = users.insert_one(user).inserted_id
        return str(user_id)
    
    @staticmethod
    def get_all():
        users = list(db.users.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return users
    
    @staticmethod
    def get_by_id(id):
        user = db.users.find_one({'_id': ObjectId(id)})
        if user:
            user['_id'] = str(user['_id'])
            return user
        return None
    
    @staticmethod
    def update(user_id, data):
        result = db.users.update_one({'_id':ObjectId(user_id)}, {'$set': data})
        return result.modified_count
    
    @staticmethod
    def delete(user_id):
        result = db.users.delete_one({'_id':ObjectId(user_id)})
        return result.deleted_count
    