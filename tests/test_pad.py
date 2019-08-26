from tests.testcase import TestCase
import csv


class TestPAD(TestCase):
    def test_pad(self):

        # https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/pad19b.zip
        with open("bobaadr.txt") as paddata:

            padreader = csv.DictReader(paddata, quotechar='"')

            for row in padreader:

                low_house_no = row['lhnd'].strip()

                if low_house_no:
                    boro_code = int(row['boro'])
                    boro_name = self.parser.borough_dict_reverse[boro_code].strip()
                    street = row['stname'].strip()
                    if row['zipcode'].strip():
                        zip = row['zipcode'].strip()
                    else:
                        zip = None

                    test_string = "{} {} {}, NY {}".format(low_house_no, street, boro_name, zip)
                    print(test_string)
                    result = self.parser.address(test_string)

                    self.assertDictEqual({
                        'PHN': low_house_no,
                        'STREET': street,
                        'BOROUGH_CODE': boro_code,
                        'BOROUGH_NAME': boro_name,
                        'ZIP': zip
                    }, result)
