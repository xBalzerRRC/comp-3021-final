"""This module defines the TestClient class.

Example:
    $ python -m unittest tests/test_client.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.2.0"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """Tests for the Client class."""

    def setUp(self):
        client_number = 1234
        first_name = "Xavier"
        last_name = "Balzer"
        email_address = "xbalzer@rrc.ca"

        self.client = Client(client_number, first_name, last_name, email_address)
        
    def test_init_object_initialized_to_correct_state(self):
        # Assert
        self.assertEqual(1234, self.client._Client__client_number)
        self.assertEqual("Xavier", self.client._Client__first_name)
        self.assertEqual("Balzer", self.client._Client__last_name)
        self.assertEqual("xbalzer@rrc.ca", self.client._Client__email_address)

    def test_init_invalid_client_number_raises_value_error(self):
        # Arrange
        client_number = "string"
        first_name = "Xavier"
        last_name = "Balzer"
        email_address = "xbalzer@rrc.ca"

        # Act
        with self.assertRaises(ValueError) as context:
            self.client = Client(client_number, first_name, last_name, email_address)

        # Assert 
        expected = "Client number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_blank_first_name_raises_value_error(self):
        # Arrange
        client_number = 1234
        first_name = "     "
        last_name = "Balzer"
        email_address = "xbalzer@rrc.ca"

        # Act
        with self.assertRaises(ValueError) as context:
            self.client = Client(client_number, first_name, last_name, email_address)

        # Assert 
        expected = "First name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_blank_last_name_raises_value_error(self):
        # Arrange
        client_number = 1234
        first_name = "Xavier"
        last_name = "    "
        email_address = "xbalzer@rrc.ca"

        # Act
        with self.assertRaises(ValueError) as context:
            self.client = Client(client_number, first_name, last_name, email_address)

        # Assert 
        expected = "Last name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_email_address_sets_default_value(self):
        # Arrange
        client_number = 1234
        first_name = "Xavier"
        last_name = "Balzer"
        email_address = "invalid"

        # Act
        self.client = Client(client_number, first_name, last_name, email_address)

        # Assert 
        expected = "email@pixell-river.com"
        actual = self.client._Client__email_address
        self.assertEqual(expected, actual)

    def test_client_number_accessor_returns_correct_state(self):
        # Act
        actual = self.client.client_number

        # Assert
        expected = 1234
        self.assertEqual(expected, actual)

    def test_first_name_accessor_returns_correct_state(self):
        # Act
        actual = self.client.first_name

        # Assert
        expected = "Xavier"
        self.assertEqual(expected, actual)   

    def test_last_name_accessor_returns_correct_state(self):
        # Act
        actual = self.client.last_name

        # Assert
        expected = "Balzer"
        self.assertEqual(expected, actual)   

    def test_email_address_accessor_returns_correct_state(self):
        # Act
        actual = self.client.email_address

        # Assert
        expected = "xbalzer@rrc.ca"
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        # Act
        actual = self.client.__str__()        

        # Assert
        expected = f"Balzer, Xavier [1234] - xbalzer@rrc.ca\n"
        self.assertEqual(expected, actual)
   
