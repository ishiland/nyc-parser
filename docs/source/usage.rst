Usage
=====

Installation
-----------

To use nycparser, first install it using pip:

.. code-block:: bash

   pip install nycparser

Parsing Addresses
----------------

The main functionality of nycparser is parsing NYC addresses into their components.

.. code-block:: python

   from nycparser import Parser
   
   parser = Parser()
   
   # Parse a simple address
   result = parser.address('100 Gold St, Manhattan, NY 10038')
   print(result)
   
   # Output:
   # {
   #    'PHN': '100',
   #    'STREET': 'GOLD ST',
   #    'BOROUGH_CODE': 1,
   #    'BOROUGH_NAME': 'MANHATTAN',
   #    'ZIP': '10038'
   # }

Address Components
----------------

The parser returns a dictionary with the following components:

* **PHN**: Property House Number (e.g., '100', '74-12')
* **STREET**: The street name (e.g., 'GOLD ST', '5TH AVE')
* **BOROUGH_CODE**: Numeric code for the borough (1-5)
* **BOROUGH_NAME**: Full name of the borough (e.g., 'MANHATTAN', 'QUEENS')
* **ZIP**: ZIP code if present in the address

Borough Codes
------------

NYC uses the following borough codes:

* 1 = Manhattan
* 2 = Bronx
* 3 = Brooklyn
* 4 = Queens
* 5 = Staten Island

The parser can recognize various forms and abbreviations of borough names:

* Manhattan: 'MANHATTAN', 'MN', 'NEW YORK'
* Bronx: 'BRONX', 'THE BRONX', 'BX'
* Brooklyn: 'BROOKLYN', 'BK', 'BKLYN', 'KINGS'
* Queens: 'QUEENS', 'QN', 'QU'
* Staten Island: 'STATEN ISLAND', 'SI', 'STATEN IS', 'RICHMOND'

Parsing BBLs
-----------

The parser can also handle BBL (Borough-Block-Lot) values:

.. code-block:: python

   from nycparser import Parser
   
   parser = Parser()
   
   # Parse a BBL
   result = parser.bbl('1004380006')
   print(result)
   
   # Output:
   # {
   #    'BOROUGH_CODE': 1,
   #    'BLOCK': 438,
   #    'LOT': 6,
   #    'BOROUGH_NAME': 'MANHATTAN'
   # }
   
   # BBLs can also include formatting characters
   result = parser.bbl('1-00438-0006')
   # Same result as above 