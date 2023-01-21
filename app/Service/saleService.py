from typing import Type
from app.Interface import saleInterface
from app import app, request, json
from wraps import panic

class SaleService:
    def __init__(self, repository: Type[saleInterface.SaleInteface]):
        self.__repository = repository

    def post_sale(self, data):
        sale = self.__repository.post_sale(self, data)
        return sale