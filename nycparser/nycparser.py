import re
from typing import Dict, Union, List, Optional, Any


class Parser:
    def __init__(self):

        self.borough_dict = {
            "MANHATTAN": 1,
            "MN": 1,
            "NEW YORK": 1,
            "BRONX": 2,
            "THE BRONX": 2,
            "BX": 2,
            "BROOKLYN": 3,
            "BK": 3,
            "BKLYN": 3,
            "KINGS": 3,
            "QUEENS": 4,
            "QN": 4,
            "QU": 4,
            "STATEN ISLAND": 5,
            "SI": 5,
            "STATEN IS": 5,
            "RICHMOND": 5,
        }

        self.borough_dict_reverse = {
            1: "MANHATTAN",
            2: "BRONX",
            3: "BROOKLYN",
            4: "QUEENS",
            5: "STATEN ISLAND",
        }

        # Additional terms to filter out from street names
        self.filter_terms = ["NEW YORK", "NY", "USA", "UNITED STATES", "AMERICA"]

        # Common street descriptors to preserve
        self.descriptors = ["REAR", "EAST", "WEST", "NORTH", "SOUTH", "FRONT"]

    def address(self, address: str) -> Dict[str, Any]:
        """
        Parses a single line input address.

        Args:
            address: A single line input address with PHN and Street, ex. "100 Gold St."

        Returns:
            A dictionary with PHN, STREET, BOROUGH_CODE, BOROUGH_NAME, ZIP

        Examples:
            >>> parser = Parser()
            >>> parser.address("100 Gold St, Manhattan, NY 10038")
            {'PHN': '100', 'STREET': 'GOLD ST', 'BOROUGH_CODE': 1, 'BOROUGH_NAME': 'MANHATTAN', 'ZIP': '10038'}
        """
        if not address or not isinstance(address, str):
            raise ValueError("Address must be a non-empty string")

        # Normalize input
        address = address.strip().upper()

        result = {
            "PHN": None,
            "STREET": "",
            "BOROUGH_CODE": None,
            "BOROUGH_NAME": None,
            "ZIP": None,
        }

        # Special case: single word input is treated as PHN
        if len(address.split()) == 1 and address.strip().replace("-", "").isdigit():
            result["PHN"] = address
            return result

        # Extract house number - handles both standard and Queens-style hyphenated house numbers
        house_match = re.match(r"^(\d+(?:-\d+)?)\s+(.+)$", address)
        if house_match:
            result["PHN"] = house_match.group(1)
            unparsed = house_match.group(2)
        else:
            # Handle addresses without house numbers
            unparsed = address

        # Extract ZIP code
        zip_match = re.search(r"\b(\d{5})(?:-\d{4})?\b", address)
        if zip_match:
            result["ZIP"] = zip_match.group(1)
            # Remove zip from unparsed
            unparsed = re.sub(r"\b\d{5}(?:-\d{4})?\b", "", unparsed)

        # Extract borough using position-based approach
        street = unparsed
        matched_borough = False
        borough_matches = []

        # Find all potential borough matches with their positions
        for borough_name, borough_code in self.borough_dict.items():
            match = re.search(r"\b{}\b".format(re.escape(borough_name)), unparsed)
            if match:
                borough_matches.append((match.start(), borough_name, borough_code))

        # Sort by position in the string (earlier matches first)
        borough_matches.sort()

        if borough_matches:
            # Use the first occurrence
            _, borough_name, borough_code = borough_matches[0]
            result["BOROUGH_CODE"] = borough_code
            result["BOROUGH_NAME"] = self.borough_dict_reverse[borough_code]
            matched_borough = True

        # Now that we found the borough, remove ALL borough names from the street string
        # This ensures names like "Queens" are removed regardless of match
        if matched_borough:
            for borough_name in self.borough_dict.keys():
                street = re.sub(r"\b{}\b".format(re.escape(borough_name)), "", street)

        # Remove apartment/unit information
        apt_patterns = [
            r",\s*(?:APT|APARTMENT|UNIT|SUITE|#)[^\d]*[\w-]+",
            r"(?:APT|APARTMENT|UNIT|SUITE|#)[^\d]*[\w-]+",
        ]

        for pattern in apt_patterns:
            street = re.sub(pattern, "", street, flags=re.IGNORECASE)

        # Remove filter terms like state, country, etc.
        for term in self.filter_terms:
            street = re.sub(r"\b{}\b".format(re.escape(term)), "", street)

        # Clean up remaining punctuation and extra spaces
        street = re.sub(r"[,\-\.\(\)]+", " ", street)
        street = re.sub(r"\s+", " ", street).strip()

        # Preserve descriptors in the correct position
        result["STREET"] = street

        return result

    def bbl(self, bbl: Union[str, int]) -> Dict[str, Any]:
        """
        Parses a single line input BBL (Borough-Block-Lot).

        Args:
            bbl: A single line input bbl. Can contain special characters, just needs 10 digits.

        Returns:
            A dictionary with BOROUGH_CODE, BLOCK, LOT and BOROUGH_NAME

        Raises:
            ValueError: If the BBL doesn't contain exactly 10 digits or has an invalid borough code.

        Examples:
            >>> parser = Parser()
            >>> parser.bbl("1-01234-0001")
            {'BOROUGH_CODE': 1, 'BLOCK': 1234, 'LOT': 1, 'BOROUGH_NAME': 'MANHATTAN'}
        """
        result = {
            "BOROUGH_CODE": None,
            "BLOCK": None,
            "LOT": None,
            "BOROUGH_NAME": None,
        }

        # Remove any special characters
        tmp = "".join(e for e in str(bbl) if e.isdigit())

        if len(tmp) != 10:
            raise ValueError(f"{bbl} is not a 10 digit BBL.")

        borough_code = int(tmp[0])
        if borough_code < 1 or borough_code > 5:
            raise ValueError(f"Invalid borough code: {borough_code}")

        result["BOROUGH_CODE"] = borough_code
        result["BLOCK"] = int(tmp[1:6])
        result["LOT"] = int(tmp[6:10])
        result["BOROUGH_NAME"] = self.borough_dict_reverse[result["BOROUGH_CODE"]]

        return result
