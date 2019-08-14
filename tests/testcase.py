import unittest
from nycparser import Parser

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = Parser()
