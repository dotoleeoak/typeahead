import os
from unittest.case import TestCase
from typeahead.config import config_test_kor
from typeahead.build_index import BuildIndex


class TestIndex(TestCase):
    def setUp(self):
        self.builder = BuildIndex(
            config_test_kor.DIR_INPUT,
            config_test_kor.DIR_OUTPUT,
            config_test_kor.VERSION,
            config_test_kor.HEAP_SIZE,
            config_test_kor.PREFIX_SIZE,
        )
        self.builder.tokenize()
        self.builder.build_index()
        self.builder.read_index()

    def test1(self):
        result = self.builder.search("아")
        ans = ["ㅇㅏㅍㅡㅈㅏㄶㅇㅏ", "ㅇㅏㄴ", "ㅇㅏㅍㅇㅔ", "ㅇㅏㅍㅇㅔㅅㅓㄴ", "ㅇㅏㅈㅜ"]
        self.assertEqual(result, ans)

    def test2(self):
        result = self.builder.search("친구")
        ans = ["ㅊㅣㄴㄱㅜㄹㅡㄹ", "ㅊㅣㄴㄱㅜㄱㅏ", "ㅊㅣㄴㄱㅜ"]
        self.assertEqual(result, ans)
