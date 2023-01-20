from abc import ABC, abstractmethod

class UserInteface(ABC):
    @abstractmethod
    def get_auth(self, email, sena):
        pass

    @abstractmethod
    def getUserAll(self):
        pass

    def getUser(self, email):
        pass

    @abstractmethod
    def geUserById(self,id):
        pass