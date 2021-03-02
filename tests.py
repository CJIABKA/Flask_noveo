import unittest
from application import app


class SomeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
