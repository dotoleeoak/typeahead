from unittest.case import TestCase
from subprocess import PIPE, run


class MyTest(TestCase):
    def test1(self):
        p = run(['python3', 'main.py'], stdout=PIPE, input='act\n$', encoding='UTF-8')
        ans = "['actually', 'act', 'acted', 'actions', 'active']\n"
        self.assertEqual(ans, p.stdout)

    def test2(self):
        p = run(['python3', 'main.py'], stdout=PIPE, input='fil\n$', encoding='UTF-8')
        ans = "['file', 'files', 'filial', 'fill', 'filled']\n"
        self.assertEqual(ans, p.stdout)
