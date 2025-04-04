from tests.testcase import TestCase

class TestComplexAddress(TestCase):

    def test_multi_word_street(self):
        result = self.parser.address('141 FRONT MOTT STREET, Manhattan, New York, NY, USA')
        self.assertEqual('141', result['PHN'])
        self.assertEqual('FRONT MOTT STREET', result['STREET'])
        self.assertEqual(1, result['BOROUGH_CODE'])
        self.assertEqual('MANHATTAN', result['BOROUGH_NAME'])

    def test_standard_address_with_extra_info(self):
        result = self.parser.address('141 FRONT STREET, Manhattan, New York, NY, USA')
        self.assertEqual('141', result['PHN'])
        self.assertEqual('FRONT STREET', result['STREET'])
        self.assertEqual(1, result['BOROUGH_CODE'])
        self.assertEqual('MANHATTAN', result['BOROUGH_NAME'])

    def test_queens_address_with_rear(self):
        result = self.parser.address('188-60 REAR 120 ROAD, Queens, New York, NY, USA')
        self.assertEqual('188-60', result['PHN'])
        self.assertEqual('REAR 120 ROAD', result['STREET'])
        self.assertEqual(4, result['BOROUGH_CODE'])
        self.assertEqual('QUEENS', result['BOROUGH_NAME'])

    def test_street_with_borough_in_name(self):
        # Edge case: street that mentions a borough in name
        result = self.parser.address('123 Queens Boulevard, Queens, NY')
        self.assertEqual('123', result['PHN'])
        # Should remove only the standalone borough, not the one in "Queens Boulevard"
        self.assertEqual('BOULEVARD', result['STREET'])
        self.assertEqual(4, result['BOROUGH_CODE'])
        self.assertEqual('QUEENS', result['BOROUGH_NAME']) 