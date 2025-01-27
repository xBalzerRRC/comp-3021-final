"""This module defines the TestBankAccount class.

Example:
    $ python -m unittest tests/test_bank_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Tests for the BankAccount class."""

    def setUp(self):
        account_number = 1234
        client_number = 1
        balance = 1000.0

        self.bankaccount = BankAccount(account_number, client_number, balance)

    def test_init_object_initialized_to_correct_state(self):
        # Assert
        self.assertEqual(1234, self.bankaccount._BankAccount__account_number)
        self.assertEqual(1, self.bankaccount._BankAccount__client_number)
        self.assertEqual(1000.0, self.bankaccount._BankAccount__balance)

    def test_init_invalid_balance_sets_default_value(self):
        # Arrange
        account_number = 1234
        client_number = 1
        balance = "string"

        # Act
        self.bankaccount = BankAccount(account_number, client_number, balance)

        # Assert 
        expected = 0.0
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_init_invalid_account_number_raises_value_error(self):
        # Arrange
        account_number = "string"
        client_number = 1
        balance = 1000.0

        # Act
        with self.assertRaises(ValueError) as context:
            self.bankaccount = BankAccount(account_number, client_number, balance)

        # Assert 
        expected = "Account number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)
        
    def test_init_invalid_client_number_raises_value_error(self):
        # Arrange
        account_number = 1234
        client_number = "string"
        balance = 1000.0

        # Act
        with self.assertRaises(ValueError) as context:
            self.bankaccount = BankAccount(account_number, client_number, balance)

        # Assert 
        expected = "Client number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    
        