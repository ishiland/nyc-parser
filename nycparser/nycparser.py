import re

class Parser:
    def __init__(self):

        self.borough_dict = {
            'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1,
            'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
            'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3,
            'QUEENS': 4, 'QN': 4, 'QU': 4,
            'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5,
        }

        self.borough_dict_reverse = {
            1: 'MANHATTAN',
            2: 'BRONX',
            3: 'BROOKLYN',
            4: 'QUEENS',
            5: 'STATEN ISLAND',
        }

    def address(self, address):
        """
        Parses a single line input address.
        :param address: a single line input address with PHN and Street, ex. "100 Gold St."
        :return: A dictionary with PHN, STREET, BOROUGH_CODE, BOROUGH_NAME, ZIP
        """
        # Split the string on whitespace and take the first item as PHN
        spl = address.split(" ")
        phn = spl[0]

        unparsed = " ".join(spl[1:]).strip().upper()

        result = {
            'PHN': phn,
            'STREET': unparsed,
            'BOROUGH_CODE': None,
            'BOROUGH_NAME': None,
            'ZIP': None
        }

        # Get the Street
        separators = [',', 'APT', 'SUITE', '#', 'UNIT', '-']
        for s in separators:
            # remove any white space and consecutive separators around separator
            rem = re.sub(r'[^\w]+{}[^\w]+'.format(s), s, unparsed)
            # find all instances of it
            fa = re.findall(r'{}.+'.format(s), rem)
            # get everything past the first string
            if len(fa):
                # replace the matching string in the original input.
                result['STREET'] = re.sub(fa[0], "", rem)

        # Get the Zip Code
        zip_code = re.findall(r'\b\d{5}', address)
        if len(zip_code):
            result['ZIP'] = zip_code[0]

        # Get the Borough
        borough = [self.borough_dict[b] for b in self.borough_dict if
                   len(re.findall(r'{}'.format(b), unparsed.upper()))]
        if len(borough):
            result['BOROUGH_CODE'] = borough[0]
            result['BOROUGH_NAME'] = self.borough_dict_reverse[result['BOROUGH_CODE']]

        return result

    def bbl(self, bbl):
        """
        Parses a single line input BBL.
        :param bbl: a single line input bbl, ex. "100 Gold St."
        :return: A dictionary with PHN, STREET, BOROUGH_CODE, BOROUGH_NAME, ZIP
        """
        result = dict()

        result['BOROUGH_CODE'] = None
        result['BLOCK'] = None
        result['LOT'] = None
        result['BOROUGH_NAME'] = None

        # remove any special characters
        tmp = ''.join(e for e in str(bbl) if e.isalnum())

        if len(tmp) == 10:
            result['BOROUGH_CODE'] = int(tmp[0])
            result['BLOCK'] = int(tmp[2:6])
            result['LOT'] = int(tmp[-4:])
            result['BOROUGH_NAME'] = self.borough_dict_reverse[result['BOROUGH_CODE']]
        else:
            raise Exception('{} is not a 10 digit BBL.'.format(bbl))

        return result
