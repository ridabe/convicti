from app import db, mm
from sqlalchemy import Column, Integer, String, Boolean, Float

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    valor_venda = db.Column(db.Float)
    vendedor_id = db.Column(db.Integer)
    unidade_id = db.Column(db.Integer)
    diretoria_id = db.Column(db.Integer)
    lat_origin = db.Column(db.String)
    lon_origin = db.Column(db.String)
    unidade_proxima = db.Column(db.Integer)
    lat_close_origin = db.Column(db.String)
    lon_close_origin = db.Column(db.String)
    tag_roming = db.Column(db.Boolean)

    def to_json(self):
        return {
                'id': self.id,
                'valor_venda': self.valor_venda,
                'vendedor_id': self.vendedor_id,
                'unidade_id': self.unidade_id,
                'diretoria_id': self.diretoria_id,
                'lat_origin': self.lat,
                'lat_origin': self.lon,
                'unidade_proxima': self.unidade_proxima,
                'lat_close_origin': self.lat_close_origin,
                'lon_close_origin': self.lon_close_origin,
                'tag_roming': self.tag_roming
        }


class SaleSchema(mm.Schema):
    class Meta:
        fields = ('id', 'data_venda', 'valor_venda', 'vendedor_id', 'unidade_id', 'diretoria_id', 'lat_origin', 'lon_origin', 'unidade_proxima', 'lat_close_origin', 'lon_close_origin', 'tag_roming')

class SaleSchemaGet(mm.Schema):
    class Meta:
        fields = ('id', 'data_venda', 'valor_venda', 'vendedor_id', 'vendedor', 'unidade_id', 'unidade', 'diretoria_id', 'nome_diretoria', 'lat_origin', 'lon_origin', 'unidade_proxima', 'lat_close_origin', 'lon_close_origin', 'tag_roming')


sale_share_schema_get = SaleSchemaGet()
sales_share_schema_get = SaleSchemaGet(many=True)
sale_share_schema = SaleSchema()
sales_share_schema = SaleSchema(many=True)


