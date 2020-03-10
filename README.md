# NYC Parser
A utility to parse NYC addresses and BBLs from a single line input. 

 [![Python 2.7 | 3.4+](https://img.shields.io/badge/python-2.7%20%7C%203.4+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Build Status](https://travis-ci.org/ishiland/nyc-parser.svg?branch=master)](https://travis-ci.org/ishiland/nyc-parser)  [![PyPI version](https://img.shields.io/pypi/v/nyc-parser.svg)](https://pypi.python.org/pypi/nyc-parser/)

## Install
```sh
$ pip install nyc-parser
```
or clone this repo, `cd` into it and
```sh
$ pip install .
```
## Usage

```python
>> from nycparser import Parser

>> p = Parser()

# Parse an address
>> p.address('74-12 35th ave, Queens NY 11372')

{'PHN': '74-12',
'STREET': '35TH AVE',
'BOROUGH_CODE': 4,
'BOROUGH_NAME': 'QUEENS',
'ZIP': '11372'}


# Parse a BBL with or without special characters, just needs 10 digits.
>> p.bbl('1-00438-0006')

{'BLOCK': 438,
'LOT': 6,
'BOROUGH_CODE': 1,
'BOROUGH_NAME': 'MANHATTAN'}


# There is also a dictionary to get Borough code from Borough Name.
>> p.borough_dict['BROOKLYN']

3


# Or you can do the reverse.
>> p.borough_dict_reverse[3]

'BROOKLYN'

```

### Contribute
Issues and PRs welcome.


### License
MIT
