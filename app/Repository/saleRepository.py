from abc import ABC
from wraps import panic
from app import app, json, Response, jsonify, db
from app.Model.saleModel import Venda
from app.Interface import saleInterface
import datetime
import jwt


class SaleRepository(saleInterface.SaleInteface, ABC):
    def post_sale(self, data):
        vendas = Venda(
            valor_venda=data['valor_venda'],
            vendedor_id=int(data["vendedor_id"]),
            unidade_id=int(data["unidade_id"]),
            diretoria_id=int(data["diretoria_id"])
        )
        try:
            db.session.add(vendas)
            db.session.commit()
            return jsonify({
                "data": vendas.to_json(),
                "message": "Criado com Sucesso"
            }), 200
        except Exception as e:
            return jsonify({
                "data": {},
                "Erro": e
            }), 400
