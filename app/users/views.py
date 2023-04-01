from flask import jsonify, request
from flask.views import MethodView
from users.controller import UserController

class PingView(MethodView):
    def get(self):
        return jsonify({'message': 'pong'})

class UserListView(MethodView):
    def get(self):
        users = UserController().get_all()
        return jsonify(users)

    def post(self):
        data = request.get_json()
        user_id = UserController().create(data)
        return jsonify({'id': user_id}), 201
    
class UserDetailView(MethodView):
    def get(self, id):
        user = UserController().get_by_id(id)
        if user:
            return jsonify(user)
        return jsonify({'message': 'User not found'}), 404
    
    def put(self, id):
        data = request.get_json()
        updated = UserController().update(id, data)
        if updated:
            return jsonify({'message': 'User updated'})
        return jsonify({'message': 'User not found'}), 404
    
    def delete(self, id):
        deleted = UserController().delete(id)
        if deleted:
            return jsonify({'message': 'User deleted'})
        return jsonify({'message': 'User not found'}), 404