from app import db, mm
from sqlalchemy import Column, Integer, String, Boolean, Float


class UnitModel(db.Model):
    __tablename__ = 'unidade'

    id = db.Column(db.Integer, primary_key=True)
    unidade = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    gerente_id = db.Column(db.Integer)
    diretoria_id = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'unidade': self.unidade,
            'lat': self.lat,
            'lon': self.lon,
            'gerente_id': self.gerente_id,
            'diretoria_id': self.diretoria_id
        }


class UnitSchema(mm.Schema):
    class Meta:
        fields = ('id', 'unidade', 'lat', 'lon', 'gerente_id', 'diretoria_id')


unit_share_schema = UnitSchema()
units_share_schema = UnitSchema(many=True)
