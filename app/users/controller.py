from .models import User

class UserController:
    def create(self, data):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user = User(name, email, password)
        return user.save()
    
    def get_all(self):
        return User.get_all()
    
    def get_by_id(self, id):
        return User.get_by_id(id)
    
    def update(self, id, data):
        return User.update(id, data)
    
    def delete(self, id):
        return User.delete(id)
    
    