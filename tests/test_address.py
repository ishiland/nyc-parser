from tests.testcase import TestCase

class TestAddress(TestCase):

    def test_phn(self):
        result = self.parser.address('100')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': '',
            'BOROUGH_CODE': None,
            'BOROUGH_NAME': None,
            'ZIP': None
        }, result)

    def test_street(self):
        result = self.parser.address('100 Gold st')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': 'GOLD ST',
            'BOROUGH_CODE': None,
            'BOROUGH_NAME': None,
            'ZIP': None
        }, result)

    def test_borough_code(self):
        result = self.parser.address('100 Gold st, mn')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': 'GOLD ST',
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
            'ZIP': None
        }, result)

    def test_borough_name(self):
        result = self.parser.address('100 Gold, mn')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': 'GOLD',
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
            'ZIP': None
        }, result)

    def test_zip(self):
        result = self.parser.address('100 Gold st, MN 10038')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': 'GOLD ST',
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
            'ZIP': '10038'
        }, result)

    def test_address_w_apartment(self):
        result = self.parser.address('100 gold st apt 123, mn')
        self.assertDictEqual({
            'PHN': '100',
            'STREET': 'GOLD ST',
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
            'ZIP': None
        }, result)

    def test_queens_address(self):
        result = self.parser.address('74-12 35th ave, Queens')
        self.assertDictEqual({
            'PHN': '74-12',
            'STREET': '35TH AVE',
            'BOROUGH_CODE': 4,
            'BOROUGH_NAME': 'QUEENS',
            'ZIP': None
        }, result)

    def test_queens_address_w_apartment(self):
        result = self.parser.address('74-12 35th ave apt 319, Queens NY 11372')
        self.assertDictEqual({
            'PHN': '74-12',
            'STREET': '35TH AVE',
            'BOROUGH_CODE': 4,
            'BOROUGH_NAME': 'QUEENS',
            'ZIP': '11372'
        }, result)

