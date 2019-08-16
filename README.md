# NYC Parser
A utility to parse NYC addresses and BBLs from a single line input. 

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

# parse an address
>> p.address('74-12 35th ave, Queens NY 11372')

{'PHN': '74-12',
'STREET': '35TH AVE',
'BOROUGH_CODE': 4,
'BOROUGH_NAME': 'QUEENS',
'ZIP': '11372'}


# parse a BBL
>> p.bbl('1004380006')

{'BLOCK': 438,
'LOT': 6,
'BOROUGH_CODE': 1,
'BOROUGH_NAME': 'MANHATTAN'}


# can contain special characters, just needs 10 digits
>> p.bbl('1-00438-0006')

{'BLOCK': 438,
'LOT': 6,
'BOROUGH_CODE': 1,
'BOROUGH_NAME': 'MANHATTAN'}

```

### License
MIT