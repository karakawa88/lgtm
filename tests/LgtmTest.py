import unittest

from lgtm import core
class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        self.assertIsNone(core.lgtm())

