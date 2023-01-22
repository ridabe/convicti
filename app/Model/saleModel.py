from app import db, mm
from sqlalchemy import Column, Integer, String, Boolean, Float

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    valor_venda = db.Column(db.Float)
    vendedor_id = db.Column(db.Integer)
    unidade_id = db.Column(db.Integer)
    diretoria_id = db.Column(db.Integer)
    lat = db.Column(db.String)
    lon = db.Column(db.String)

    def to_json(self):
        return {
                'id': self.id,
                'valor_venda': self.valor_venda,
                'vendedor_id': self.vendedor_id,
                'unidade_id': self.unidade_id,
                'diretoria_id': self.diretoria_id,
                'lat': self.lat,
                'lon': self.lon
        }


class SaleSchema(mm.Schema):
    class Meta:
        fields = ('id', 'data_venda', 'valor_venda', 'vendedor_id', 'unidade_id', 'diretoria_id', 'lat', 'lon')

class SaleSchemaGet(mm.Schema):
    class Meta:
        fields = ('id', 'data_venda', 'valor_venda', 'vendedor_id', 'vendedor', 'unidade_id', 'unidade', 'diretoria_id', 'nome_diretoria', 'lat', 'lon')


sale_share_schema_get = SaleSchemaGet()
sales_share_schema_get = SaleSchemaGet(many=True)
sale_share_schema = SaleSchema()
sales_share_schema = SaleSchema(many=True)


