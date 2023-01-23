from abc import ABC, abstractmethod

class SaleInteface(ABC):
    @abstractmethod
    def post_sale(self, data):
        pass

    @abstractmethod
    def get_sales(self, current_user):
        pass

    @abstractmethod
    def get_unit(self, diretoria_id):
        pass

    @abstractmethod
    def get_unit_by_id(self, id):
        pass
