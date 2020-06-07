import os
from unittest.case import TestCase
from typeahead.config import config_test
from typeahead.build_index import BuildIndex


class TestIndex(TestCase):
    def setUp(self):
        self.builder = BuildIndex(
            config_test.DIR_INPUT,
            config_test.DIR_OUTPUT,
            config_test.VERSION,
            config_test.HEAP_SIZE,
            config_test.PREFIX_SIZE,
        )
        self.builder.tokenize()
        self.builder.build_index()
        self.builder.tokenize()
        self.builder.read_index()

    def test1(self):
        with open("word-count.txt", "r") as f1:
            w1 = f1.readlines()
        with open("test/word-count-en.txt", "r") as f2:
            w2 = f2.readlines()
        self.assertEqual(w1, w2)

    def test2(self):
        result = self.builder.search("act")
        ans = ["actually", "act", "actual", "active", "actions"]
        self.assertEqual(result, ans)

    def test3(self):
        result = self.builder.search("haste")
        ans = ["haste", "hastened", "hastening", "hasten"]
        self.assertEqual(result, ans)

    def test4(self):
        result = self.builder.search("i")
        ans = ["it", "i", "in", "is", "if"]
        self.assertEqual(result, ans)
