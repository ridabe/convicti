from typing import Type
from app.Interface import saleInterface
from app import app, request, json
from wraps import panic
from app.Helper.calculate_distance import getDistanceBetweenPointsNew


class SaleService:
    def __init__(self, repository: Type[saleInterface.SaleInteface]):
        self.__repository = repository

    def post_sale(self, data):
        lat = data['lat']
        lon = data['lon']
        panic(lon)
        distance = getDistanceBetweenPointsNew()
        sale = self.__repository.post_sale(self, data)
        return sale

    def get_sales(self, current_user):
        sales = self.__repository.get_sales(self, current_user)
        return sales
