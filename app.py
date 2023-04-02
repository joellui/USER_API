from bson import ObjectId
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['userDB']

# test
@app.route('/', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

# create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')

    # check if email already exists
    existing_user = db['users'].find_one({'email': email})
    if existing_user:
        return jsonify({'error': 'User with the email {} already exists'.format(email)}), 409
    
    # create user
    db.users.insert_one(data)
    return jsonify({'message': 'User created successfully!'}), 201

# get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.users.find()
    result = []
    for user in users:
        result.append({'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']})
    return jsonify(result), 200

# get user by id
@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    user = db.users.find_one({'_id': ObjectId(id)})
    if user:
        result = {'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']}
        return jsonify(result), 200
    
# update user by id
@app.route('/users/<id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.json
    result = db.users.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count > 0:
        message = {'message': 'User updated successfully!'}
        code = 200
    else:
        message = {'message': 'User not updated!'}
        code = 400
    return jsonify(message), code

# delete user by id
@app.route('/users/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    result = db.users.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        message = {'message': 'User deleted successfully!'}
        code = 200
    else:
        message = {'message': 'User not deleted!'}
        code = 400
    return jsonify(message), code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')