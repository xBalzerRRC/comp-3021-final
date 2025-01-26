"""This module defines the TestClient class.

Example:
    $ python -m unittest tests/test_client.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """Tests for the Client class."""

    def SetUp(self):
        client_number = 1234
        first_name = "Xavier"
        last_name = "Balzer"
        email_address = "xbalzer@rrc.ca"

        self.client = Client(client_number, first_name, 
                             last_name, email_address)
        
        