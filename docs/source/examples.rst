Examples
========

This page provides examples of using the NYC Parser for various address formats.

Simple Addresses
---------------

.. code-block:: python

   from nycparser import Parser
   
   parser = Parser()
   
   # Basic address
   result = parser.address('100 Gold St')
   # {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': None, 'BOROUGH_NAME': None, 'ZIP': None}
   
   # With borough
   result = parser.address('100 Gold St, Manhattan')
   # {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}
   
   # With ZIP
   result = parser.address('100 Gold St, Manhattan 10038')
   # {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': '10038'}

Complex Addresses
----------------

The parser can handle many complex address formats:

.. code-block:: python

   # Queens-style address with hyphenated house number
   result = parser.address('74-12 35th Ave, Queens')
   # {'PHN': '74-12', 'STREET': '35TH AVE', 'BOROUGH_CODE': 4, 'BOROUGH_NAME': 'QUEENS', 'ZIP': None}
   
   # Address with apartment
   result = parser.address('100 Gold St apt 123, Manhattan')
   # {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}
   
   # Complex address with descriptors
   result = parser.address('188-60 REAR 120 ROAD, Queens, New York, NY, USA')
   # {'PHN': '188-60', 'STREET': 'REAR 120 ROAD', 'BOROUGH_CODE': 4, 'BOROUGH_NAME': 'QUEENS', 'ZIP': None}
   
   # Multi-word street
   result = parser.address('141 FRONT MOTT STREET, Manhattan, New York, NY, USA')
   # {'PHN': '141', 'STREET': 'FRONT MOTT STREET', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': None}

BBL Examples
-----------

Parse Borough-Block-Lot (BBL) identifiers:

.. code-block:: python

   # Standard BBL format
   result = parser.bbl('1004380006')
   # {'BOROUGH_CODE': 1, 'BLOCK': 438, 'LOT': 6, 'BOROUGH_NAME': 'MANHATTAN'}
   
   # BBL with separators
   result = parser.bbl('1-00438-0006')
   # {'BOROUGH_CODE': 1, 'BLOCK': 438, 'LOT': 6, 'BOROUGH_NAME': 'MANHATTAN'}
   
   # Invalid BBL will raise an exception
   try:
       result = parser.bbl('100438006')  # Only 9 digits
   except ValueError as e:
       print(e)  # "100438006 is not a 10 digit BBL." 