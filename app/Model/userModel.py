from app import db, mm
from sqlalchemy import Column, Integer, String, Boolean
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __table__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    unidade_id = db.Column(db.Integer)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    nivel = db.Column(db.Integer)

    def to_json(self):
        return {'id': self.id, 'nome': self.nome, 'unidade_id': self.unidade_id, 'email': self.email, 'senha': self.senha, 'nivel': self.nivel}


    class UserSchema(mm.Schema):
        class Meta:
            fields = ('id', 'nome', 'unidade_id', 'email', 'nivel')

    user_share_schema = UserSchema()
    users_share_schema = UserSchema(many=True)