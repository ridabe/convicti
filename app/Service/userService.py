from typing import Type
from app.Interface import userInterface
from app import app, request, json
from wraps import panic


class UserService:
    def __init__(self, repository: Type[userInterface.UserInteface]):
        self.__repository = repository

    def get_auth(self, email, senha):
        auth = self.__repository.get_auth(self, email, senha)
        return auth

    def getUserAll(self):
        users = self.__repository.getUserAll(self)
        return users

    def getUserById(self, id):
        user = self.__repository.geUserById(self, id)
        return user
