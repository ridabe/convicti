from app import app, request
from app.Controller import userController, saleController
from app import authenticate
from app.Model.saleModel import Venda, sale_share_schema


@app.route('/auth', methods=['POST'])
def auth():
    senha = request.json['senha']
    email = request.json['email']
    return userController.get_auth(email, senha)


@app.route('/')
@authenticate.token_required
def get_user_all(current_user):
    return userController.get_user_all()


@app.route('/user/<id>')
@authenticate.token_required
def get_user_by_id(id, current_user):
    return userController.get_user_by_id(id)

#Rotas para vendas
@app.route('/post_vendas', methods=["POST"])
@authenticate.token_required
def post_sale(current_user):
    body = request.get_json()
    response = saleController.post_sale(body)
    return response

@app.route('/get_vendas', methods=["GET"])
@authenticate.token_required
def get_sales(current_user):
    response = saleController.get_sales(current_user)
    return response

