.. nycparser documentation master file, created by
   sphinx-quickstart on Fri Apr  4 12:17:04 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NYC Parser Documentation
=========================

**nycparser** is a Python package for parsing New York City addresses and BBL (Borough-Block-Lot) values.

Features
--------

* Parse NYC addresses into components (house number, street name, borough, zip)
* Support for Queens-style hyphenated house numbers
* Borough code identification
* BBL (Borough-Block-Lot) parsing
* Handling of complex addresses with descriptors (REAR, FRONT, etc.)

Installation
-----------

.. code-block:: bash

   pip install nycparser

Basic Usage
----------

.. code-block:: python

   from nycparser import Parser
   
   parser = Parser()
   
   # Parse an address
   result = parser.address('123 Main St, Manhattan, NY 10001')
   print(result)
   # {'PHN': '123', 'STREET': 'MAIN ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': '10001'}
   
   # Parse a BBL
   result = parser.bbl('1-01234-0001')
   print(result)
   # {'BOROUGH_CODE': 1, 'BLOCK': 1234, 'LOT': 1, 'BOROUGH_NAME': 'MANHATTAN'}

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   usage
   api
   examples

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
