from datetime import datetime
from flask import Response
from wraps import panic
from app import app, request, jsonify
import jwt
from functools import wraps
from app.Service.userService import UserService
from app.Interface import userInterface
from app.Repository import userRepository
from app.Model.userModel import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({"error": "Sem permissão de acesso."}), 403

        if not 'Bearer' in token:
            return jsonify({"error": "token inválido."}), 403

        try:
            token_pure = token.replace("Bearer", "")
            decoded = jwt.decode(token_pure, app.config['SECRETE_KEY'], algorithms="HS256")
            current_user = User.query.get(decoded['id'])
        except:
            return jsonify({"error": "token inválido."}), 403

        return f(current_user=current_user, *args, **kwargs)

    return decorated
