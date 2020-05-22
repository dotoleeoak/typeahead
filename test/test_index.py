from unittest.case import TestCase
from typeahead import main

class MyTest(TestCase):
    def test1(self):
        main.tokenize("1342-0.txt")
        with open("word-count.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/word-count.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1, w2)

    def test2(self):
        main.build_index(5)
        with open("index.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/index.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1[1:], w2[1:])

    def test3(self):
        command = 'act fil ab'
        result = main.main(command)
        # ans = [['actually', 'act', 'acted', 'actions', 'active'],
        #         ['file', 'files', 'filial', 'fill', 'filled'],
        #         ['about', 'able', 'absence', 'above', 'absolutely']]
        ans = [['actually', 'act', 'actual', 'active', 'actions'],
            ['filling', 'files', 'file', 'filled', 'fill'],
            ['able', 'absence', 'about', 'above', 'absolutely']]
        self.assertEqual(ans, result)
