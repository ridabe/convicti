from app import db, mm
from sqlalchemy import Column, Integer, String, Boolean, Float

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    valor_venda = db.Column(db.Float)
    vendedor_id = db.Column(db.Integer)
    unidade_id = db.Column(db.Integer)
    diretoria_id = db.Column(db.Integer)

    def to_json(self):
        return {
                'id': self.id,
                'valor_venda': self.valor_venda,
                'vendedor_id': self.vendedor_id,
                'unidade_id': self.unidade_id,
                'diretoria_id': self.diretoria_id
        }


class SaleSchema(mm.Schema):
    class Meta:
        fields = ('id', 'valor_venda', 'vendedor_id', 'unidade_id', 'diretoria_id')


sale_share_schema = SaleSchema()
sales_share_schema = SaleSchema(many=True)


