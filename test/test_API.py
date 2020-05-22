from unittest.case import TestCase
from config import CONFIG
from typeahead import app, main

class Test_API(TestCase):
    def setUp(self):
        main.tokenize(CONFIG["filename"])
        main.build_index(CONFIG["pq_size"])
        main.preprocess()
        self.app = app.app.test_client()

    def test1(self):
        response = self.app.get('/')
        self.assertEqual(response.json, CONFIG)
        self.assertEqual(200, response.status_code)

    def test2(self):
        response = self.app.get('/search/ab')
        self.assertEqual(response.json, 
            {"ab": ["able", "absence", "about", "above", "absolutely"]})
