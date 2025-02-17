"""This module defines the TestSavingsAccount class.

Example:
    $ python -m unittest tests/test_savings_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

import unittest
from bank_account.bank_account import BankAccount
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):
    """Tests the SavingsAccountClass."""

    def setUp(self) -> None:
        self.BASE_SERVICE_CHARGE = 0.50
        self.account_number = 1234
        self.client_number = 1
        self.balance = 1000.0
        self.date_created = date(2024, 1, 1)
        self.minimum_balance = 500

        self.bank_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
            )
        
    def test_init_object_initialized_to_correct_state(self):
        # Assert
        # Superclass private attributes
        self.assertEqual(self.account_number, 
                         self.bank_account._BankAccount__account_number)
        self.assertEqual(self.client_number, 
                         self.bank_account._BankAccount__client_number)
        self.assertEqual(self.balance, self.bank_account._BankAccount__balance)
        
        # Superclass protected attribute 
        self.assertEqual(self.date_created, self.bank_account._date_created)
                         
        # Subclass private attribute
        self.assertEqual(self.minimum_balance, 
                         self.bank_account._SavingsAccount__minimum_balance)
        
    def test_init_minimum_balance_invalid_type_initialize_state(self):
        # Arrange
        self.minimum_balance = "string"
        self.bank_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
            )
        
        # Assert
        expected = 50
        actual = self.bank_account._SavingsAccount__minimum_balance
        self.assertEqual(expected, actual)

    def test_get_service_charges_when_balance_above_minimum(self):
        # Arrange
        self.bank_account._BankAccount__balance = 1000.0

        # Act
        expected = 0.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_when_balance_equals_minimum(self):
        # Arrange
        self.bank_account._BankAccount__balance = 500.0

        # Act
        expected = 0.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_when_balance_below_minimum(self):
        # Arrange     
        self.bank_account._BankAccount__balance = 250.0

        # Act
        expected = 1
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)


    def test_str_returns_string_representation(self):
        # Act
        actual = self.bank_account.__str__()        

        # Assert
        expected = (f"Account Number: 1234 Balance: $1,000.00\n"
                    "Minimum Balance: $500.00 Account Type: Savings")
        self.assertEqual(expected, actual)
