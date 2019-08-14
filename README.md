# NYC Parser
A utility to parse NYC addresses from a single line input. Returns a dictionary with PHN, STREET, BOROUGH_CODE, BOROUGH_NAME, ZIP if values are present.

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

>> p.address('74-12 35th ave, Queens NY 11372')

{'PHN': '74-12',
'STREET': '35TH AVE',
'BOROUGH_CODE': 4,
'BOROUGH_NAME': 'QUEENS',
'ZIP': '11372'}
```


### Contribute
Please do, issues and PRs welcome.


### License
MIT