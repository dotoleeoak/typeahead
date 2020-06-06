import json
from unittest.case import TestCase
from typeahead import app


class Test_API(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test1(self):
        response = self.app.get("/")
        self.assertEqual(200, response.status_code)

    def test2(self):
        response = self.app.get("/healthcheck")
        self.assertEqual(response.get_data().decode("utf-8"), "status OK.")

    def test3(self):
        response = self.app.get("/search/ab")
        data = response.get_data().decode("utf-8")
        result = data.strip("][").split(", ")
        result = [word.strip("'") for word in result]
        self.assertEqual(
            result, ["able", "absence", "about", "above", "absolutely"],
        )
