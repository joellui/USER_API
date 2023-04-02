from flask import Flask
from flask_restful import Api
from app.users.views import UserListView, UserDetailView, PingView

app = Flask(__name__)
api = Api(app)

api.add_resource(PingView, '/')

api.add_resource(UserListView, '/users')
api.add_resource(UserDetailView, '/users/<id>')


if __name__ == '__main__':
    app.run(debug=True)