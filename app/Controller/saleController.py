from app import app, request, jsonify, Response
from app.Service.saleService import SaleService
from app.Repository.saleRepository import SaleRepository
from app import authenticate
from datetime import datetime
from app.Model.saleModel import sale_share_schema, sales_share_schema
from wraps import panic

def post_sale(data):

    try:
        sales = SaleService(SaleRepository)
        sale = sales.post_sale(data)
        return sale_share_schema.dumps(sale)
    except Exception as e:
        return jsonify({"error": e}), 400