# NYC Parser

A Python utility for parsing New York City addresses and BBL (Borough-Block-Lot) values from a single line input.

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/) [![Documentation Status](https://readthedocs.org/projects/nyc-parser/badge/?version=latest)](https://nyc-parser.readthedocs.io/en/latest/?badge=latest) [![GitHub Actions](https://github.com/ishiland/nyc-parser/actions/workflows/python-tests.yml/badge.svg)](https://github.com/ishiland/nyc-parser/actions/workflows/python-tests.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

* Parse NYC addresses into components (house number, street name, borough, zip)
* Support for Queens-style hyphenated house numbers
* Borough code identification from various name formats and abbreviations
* BBL (Borough-Block-Lot) parsing with or without separators
* Handling of complex addresses with descriptors (REAR, FRONT, etc.)
* Multi-word street names

## Installation

```sh
pip install nyc-parser
```

## Usage

### Parsing Addresses

```python
from nycparser import Parser

parser = Parser()

# Basic address
result = parser.address('100 Gold St, Manhattan')
print(result)
# {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}

# With ZIP code
result = parser.address('100 Gold St, Manhattan 10038')
print(result)
# {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': '10038'}

# Queens-style address with hyphenated house number
result = parser.address('74-12 35th Ave, Queens NY 11372')
print(result)
# {'PHN': '74-12', 'STREET': '35TH AVE', 'BOROUGH_CODE': 4, 'BOROUGH_NAME': 'QUEENS', 'ZIP': '11372'}
```

### Complex Addresses

```python
# Address with apartment
result = parser.address('100 Gold St apt 123, Manhattan')
print(result)
# {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}

# Complex address with descriptors
result = parser.address('188-60 REAR 120 ROAD, Queens, New York, NY, USA')
print(result)
# {'PHN': '188-60', 'STREET': 'REAR 120 ROAD', 'BOROUGH_CODE': 4, 'BOROUGH_NAME': 'QUEENS', 'ZIP': None}

# Multi-word street
result = parser.address('141 FRONT MOTT STREET, Manhattan, New York, NY, USA')
print(result)
# {'PHN': '141', 'STREET': 'FRONT MOTT STREET', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}
```

### Parsing BBLs

```python
# Parse a BBL with or without special characters
result = parser.bbl('1-00438-0006')
print(result)
# {'BOROUGH_CODE': 1, 'BLOCK': 438, 'LOT': 6, 'BOROUGH_NAME': 'MANHATTAN'}

# Standard BBL format (10 digits)
result = parser.bbl('1004380006')
print(result)
# {'BOROUGH_CODE': 1, 'BLOCK': 438, 'LOT': 6, 'BOROUGH_NAME': 'MANHATTAN'}
```

### Borough Dictionary

```python
# Get borough code from name
borough_code = parser.borough_dict['BROOKLYN']
print(borough_code)  # 3

# Get borough name from code
borough_name = parser.borough_dict_reverse[3]
print(borough_name)  # 'BROOKLYN'
```

## Documentation

Full documentation is available at [nyc-parser.readthedocs.io](https://nyc-parser.readthedocs.io/)

## Contributing

Issues and PRs are welcome! Please feel free to contribute to this project.

## License

MIT
