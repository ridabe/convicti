from app import app, request
from app.Controller import userController
from app import authenticate

@app.route('/auth', methods=['POST'])
def auth():
    senha = request.json['senha']
    email = request.json['email']
    return userController.get_auth(email, senha)

@app.route('/')
@authenticate.token_required
def get_user_all(current_user):
    return userControl.get_user_all()

@app.route('/user/<email>')
@authenticate.token_required
def get_user(email, current_user):
    return userController.get_user(email)
