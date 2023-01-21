from app import app, request, jsonify, Response
from app.Service.userService import UserService
from app.Repository.userRepository import UserRepository
from app.Dto import userDto
from app import authenticate
from datetime import datetime
from app.Model.userModel import user_share_schema, users_share_schema
from wraps import panic


def get_auth(email, senha):
    users = UserService(UserRepository)
    auth = users.get_auth(email, senha)
    return auth


def get_user_all():
    try:
        users = UserService(UserRepository)
        user = users.getUserAll()
        return users_share_schema.dumps(
            user
        )
    except:
        return userDto(401, {}, "usuarios nao encontrados")


def get_user_by_id(id):
    try:
        users = UserService(UserRepository)
        user = users.getUserById(id)
        if user:
            status = 200
            message = "Success"
            return user_share_schema.dumps(user)
    except:
        return userDto(401, {}, "usuarios nao encontrados")
