from unittest.case import TestCase
from typeahead import app


class Test_API(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test1(self):
        response = self.app.get('/')
        self.assertEqual(response.json, app.config)
        self.assertEqual(200, response.status_code)

    def test2(self):
        response = self.app.get('/search/ab')
        self.assertEqual(response.json,
                         {"ab": ["able", "absence", "about", "above", "absolutely"]})
