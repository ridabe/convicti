
from app import app, request, os
from app.Helper.calculate_distance import getDistanceBetweenPointsNew
import unittest


class TestCalculateDistance(unittest.TestCase):
    def test_should_return_distance_in_km(self):
        lat_origin = "-19.947854829716372"
        lon_origin = "-43.94089385954766"
        lat_unidade = "-19.917854829716372"
        lon_unidade = "-43.94089385954766"
        response = getDistanceBetweenPointsNew(float(lat_origin), float(lon_origin), float(lat_unidade),
                                               float(lon_unidade))
        expected = 136
        self.assertEqual(response, expected)


if __name__ == "__name__":
    unittest.main
