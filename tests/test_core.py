import unittest

from lgtm import core

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        self.assertIsNone(core.lgtm())

    def test_func(self):
        dic = {
            'name': 'Robin Footer',
            'stock': 12800
        };
        data = '';
        for key, val in dic.items():
            data = data + f'key={key}, value={val}\n'
        result = core.func(**dic)
        self.assertEqual(data, result)



