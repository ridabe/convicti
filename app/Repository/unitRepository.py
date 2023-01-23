from abc import ABC
from wraps import panic
from app import app, json, Response, jsonify
from app.Model.unitMdel import UnitModel, unit_share_schema, units_share_schema
from app.Interface import unitInterface
from app.Dto import userDto
import datetime
import jwt

class UniteRepository(unitInterface.UnitInterface, ABC):

    def get_units_by_director_id(self, director_id):
        user_object = UnitModel.query.get_by(dretoria_id=director_id)
        user_json = [user.to_json() for user in user_object]
        return user_json