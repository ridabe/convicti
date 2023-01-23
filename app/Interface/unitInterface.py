from abc import ABC, abstractmethod


class UnitInterface(ABC):

    @abstractmethod
    def get_units_by_director_id(self, director_id):
        pass
