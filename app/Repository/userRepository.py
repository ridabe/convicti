from abc import ABC
from wraps import panic
from app import app, json, Response, jsonify
from app.Model.userModel import User
from app.Interface import userInterface
from app.Dto import userDto
import datetime
import jwt


class UserRepository(userInterface.UserInteface, ABC):
    def get_auth(self, email, senha):
        user_object = User.query.filter_by(email=email).first()
        if not user_object:
            return jsonify({'message': 'user not found', 'data': {}}), 401

        user_json = user_object.to_json()

        if senha == user_json["senha"]:
            payload = {
                "id": user_json["id"],
                "email": user_json["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({
                "token": token
            })
        return jsonify({"message": 'could not verify', 'www-authenticate': 'Basic auth="Login required"'}), 403

    def getUserAll(self):
        user_object = User.query.all()
        user_json = [user.to_json() for user in user_object]
        return user_json

    def geUserById(self, id):
        user_object = User.query.get(id)
        user_json = user_object.to_json()
        return user_json

