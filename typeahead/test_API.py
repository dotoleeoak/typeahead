from unittest.case import TestCase
from config import CONFIG
from app import app
import main
import pytest
import requests

class Test_API(TestCase):
    def setUp(self):
        main.tokenize(CONFIG["filename"])
        main.build_index(CONFIG["pq_size"])
        main.preprocess()
        self.app = app.test_client()

    def test1(self):
        response = self.app.get('/')
        self.assertEqual(response.json, CONFIG)
        self.assertEqual(200, response.status_code)

    def test2(self):
        response = self.app.get('/search/ab')
        self.assertEqual(response.json, 
            {"ab": ["able", "absence", "about", "above", "absolutely"]})
