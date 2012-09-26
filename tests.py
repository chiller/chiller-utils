import random
import unittest
import chiller_utils
class TestMailcatch(unittest.TestCase):


    def test_shuffle(self):
        self.assertTrue(chiller_utils.check_mailcatch("e@mailcatch.com"))


if __name__ == '__main__':
    unittest.main()