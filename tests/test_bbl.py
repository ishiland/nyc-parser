from tests.testcase import TestCase


class TestBBL(TestCase):
    def test_has_values(self):
        result = self.parser.bbl('1004380006')
        self.assertDictEqual({
            'BLOCK': 438,
            'LOT': 6,
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
        }, result)

    def test_invalid_bbl(self):
        with self.assertRaises(Exception) as context:
            invalid_bbl = '100438006'
            result = self.parser.bbl(invalid_bbl)
            self.assertTrue('{} is not a 10 digit BBL.'.format(invalid_bbl) in context.exception)
            self.assertDictEqual({
                'BLOCK': None,
                'LOT': None,
                'BOROUGH_CODE': None,
                'BOROUGH_NAME': None,
            }, result)

    def test_remove_special_characters(self):
        result = self.parser.bbl('1-00438-0006')
        self.assertDictEqual({
            'BLOCK': 438,
            'LOT': 6,
            'BOROUGH_CODE': 1,
            'BOROUGH_NAME': 'MANHATTAN',
        }, result)
