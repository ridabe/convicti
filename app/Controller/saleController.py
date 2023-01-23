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
        return {"message": "ok"}
    except Exception as e:
        panic(e)
        return jsonify({"error": "nao gravou"}), 400

def get_sales(current_user):
    get_sales = SaleService(SaleRepository)
    get_sale = get_sales.get_sales(current_user)
    return get_sale
