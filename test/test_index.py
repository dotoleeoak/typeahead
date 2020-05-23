from unittest.case import TestCase
from typeahead.build_index import BuildIndex
from typeahead.config import config


class TestIndex(TestCase):
    # FIXME: Have to fix config first.
    builder = BuildIndex(**config)

    def test1(self):
        self.builder.tokenize()
        with open("word-count.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/word-count.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1, w2)

    def test2(self):
        self.builder.build_index()
        with open("index.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/index.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1[1:], w2[1:])

    def test3(self):
        self.builder.read_index()
        result = self.builder.typeahead['act']
        ans = ['actually', 'act', 'actual', 'active', 'actions']
        self.assertEqual(result, ans)

    def test4(self):
        result = self.builder.typeahead['haste']
        ans = ['haste', 'hastened', 'hastening', 'hasten']
        self.assertEqual(result, ans)

    def test5(self):
        result = self.builder.typeahead['i']
        ans = ['it', 'i', 'in', 'is', 'if']
        self.assertEqual(result, ans)
