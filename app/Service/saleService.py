from typing import Type
from app.Interface import saleInterface, unitInterface
from app import app, request, json
from wraps import panic
from app.Helper.calculate_distance import getDistanceBetweenPointsNew


class SaleService:
    def __init__(self, repository: Type[saleInterface.SaleInteface]):
        self.__repository = repository

    def post_sale(self, data):
        id_min_value = self.get_min_value_between_distance(data)
        if id_min_value != 0:
            unit_position = self.__repository.get_unit_by_id(self, id_min_value)
            data['lat_close_origin'] = unit_position[0]['lat']
            data['lon_close_origin'] = unit_position[0]['lon']
            data['unidade_proxima'] = id_min_value
            data['tag_roming'] = True
        else:
            data['lat_close_origin'] = "null"
            data['lon_close_origin'] = "Null"
            data['unidade_proxima'] = 0
            data['tag_roming'] = False

        sale = self.__repository.post_sale(self, data)
        return sale

    def get_sales(self, current_user):
        sales = self.__repository.get_sales(self, current_user)
        return sales

    def get_min_value_between_distance(self, data):
        lat_orgin = data['lat_origin']
        lon_origin = data['lon_origin']
        units = self.__repository.get_unit(self, data["diretoria_id"])
        distance = dict({
            "id": [],
            "Distance": []
        })
        distance_list = []
        for unidade in units:
            lat_unidade = unidade['lat']
            lon_unidade = unidade['lon']
            distance["id"].append(unidade['id'])
            distance["Distance"].append(
                getDistanceBetweenPointsNew(float(lat_orgin), float(lon_origin), float(lat_unidade),
                                            float(lon_unidade)))

        list_id = distance['id']
        list_distance = distance['Distance']
        union_list_to_dict = dict(zip(list_id, list_distance))

        value_min = union_list_to_dict[min(union_list_to_dict, key=union_list_to_dict.get)]
        if value_min > 0:
            for data in union_list_to_dict:
                if union_list_to_dict[data] == value_min:
                    value_min_key = data
            return value_min_key
        else:
            value_min_key = 0

        return value_min_key
