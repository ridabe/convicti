import types
from abc import ABC
from typing import Type

import sqlalchemy
from sqlalchemy import engine
from wraps import panic
from app import app, json, Response, jsonify, db
from app.Model.saleModel import Venda, sale_share_schema, sales_share_schema, sales_share_schema_get
from app.Model.userModel import User
from app.Model.unitMdel import UnitModel, units_share_schema, unit_share_schema
from app.Interface import saleInterface
from app.Dto.postSaleDto import post_sale_dto
import datetime
from sqlalchemy.sql import text

DIRETOR_GERAL = 1
DIRETOR = 2
GERENTE = 3
VENDEDOR = 4


def Get_level(id):
    user_object = User.query.get(id)
    user_json = user_object.to_json()
    nivel = user_json['nivel']
    return nivel


def Get_sales_general_manager():
    sql = f"""select 
            v.id,
            v.data_venda, 
            v.diretoria_id,
            d.nome_diretoria,
            v.unidade_id,
            un.unidade,
            v.vendedor_id,
            u.nome as vendedor,
            v.valor_venda
            from vendas as v
            inner join diretoria as d on d.id = v.diretoria_id 
            inner join unidade as un on un.id = v.unidade_id 
            inner Join usuario as u on u.id = v.vendedor_id 
            where 1"""
    result = db.session.execute(sqlalchemy.text(sql))
    response = json.loads(sales_share_schema_get.dumps(result.all()))
    return response


def Get_sales_salesman(id):
    sql = f"""select 
               v.id,
               v.data_venda, 
               v.diretoria_id,
               d.nome_diretoria,
               v.unidade_id,
               un.unidade,
               v.vendedor_id,
               u.nome as vendedor,
               v.valor_venda
               from vendas as v
               inner join diretoria as d on d.id = v.diretoria_id 
               inner join unidade as un on un.id = v.unidade_id 
               inner Join usuario as u on u.id = v.vendedor_id 
               where v.vendedor_id ={id}"""
    result = db.session.execute(sqlalchemy.text(sql))
    response = json.loads(sales_share_schema_get.dumps(result.all()))
    return response

def Get_sales_director(id):
    sql = f"""select 
                   v.id,
                   v.data_venda, 
                   v.diretoria_id,
                   d.nome_diretoria,
                   v.unidade_id,
                   un.unidade,
                   v.vendedor_id,
                   u.nome as vendedor,
                   v.valor_venda
                   from vendas as v
                   inner join diretoria as d on d.id = v.diretoria_id 
                   inner join unidade as un on un.id = v.unidade_id 
                   inner Join usuario as u on u.id = v.vendedor_id 
                   where d.diretor_id ={id}"""
    result = db.session.execute(sqlalchemy.text(sql))
    response = json.loads(sales_share_schema_get.dumps(result.all()))
    return response


def Get_sales_manager(id):
    sql = f"""select 
                   v.id,
                   v.data_venda, 
                   v.diretoria_id,
                   d.nome_diretoria,
                   v.unidade_id,
                   un.unidade,
                   v.vendedor_id,
                   u.nome as vendedor,
                   v.valor_venda
                   from vendas as v
                   inner join diretoria as d on d.id = v.diretoria_id 
                   inner join unidade as un on un.id = v.unidade_id 
                   inner Join usuario as u on u.id = v.vendedor_id 
                   where un.gerente_id ={id}"""
    result = db.session.execute(sqlalchemy.text(sql))
    response = json.loads(sales_share_schema_get.dumps(result.all()))
    return response


class SaleRepository(saleInterface.SaleInteface, ABC):
    def post_sale(self, data):
        vendas = Venda(
            valor_venda=data['valor_venda'],
            vendedor_id=int(data["vendedor_id"]),
            unidade_id=int(data["unidade_id"]),
            diretoria_id=int(data["diretoria_id"]),
            lat_origin=data['lat_origin'],
            lon_origin=data['lon_origin'],
            unidade_proxima=data['unidade_proxima'],
            lat_close_origin=data['lat_close_origin'],
            lon_close_origin=data['lon_close_origin'],
            tag_roming=data['tag_roming']
        )
        try:
            db.session.add(vendas)
            db.session.commit()
            return post_sale_dto(200, vendas, "Success")
        except Exception as e:
            return jsonify({
                "data": {},
                "Erro": "erro"
            }), 400

    def get_sales(self, current_user):
        current_user_str = sale_share_schema.dumps(current_user)
        current_user_json = json.loads(current_user_str)
        level = Get_level(current_user_json['id'])
        id = current_user_json['id']

        if level == DIRETOR_GERAL:
            return Get_sales_general_manager()
        elif level == DIRETOR:
            return Get_sales_director(id)
        elif level == GERENTE:
            return Get_sales_manager(id)
        elif level == VENDEDOR:
            return Get_sales_salesman(id)

    def get_unit(self, diretoria_id):
        sql = f"""select id, unidade, lat, lon from unidade where diretoria_id ={diretoria_id}"""
        result = db.session.execute(sqlalchemy.text(sql))
        response = json.loads(units_share_schema.dumps(result.all()))
        return response

    def get_unit_by_id(self, id):
        sql = f"""select lat, lon from unidade where id ={id}"""
        result = db.session.execute(sqlalchemy.text(sql))
        response = json.loads(units_share_schema.dumps(result.all()))
        return response
