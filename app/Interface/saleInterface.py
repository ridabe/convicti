from abc import ABC, abstractmethod

class SaleInteface(ABC):
    @abstractmethod
    def post_sale(self, data):
        pass