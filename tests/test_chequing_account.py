"""This module defines the TestChequingAccount class.

Example:
    $ python -m unittest tests/test_chequing_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.0.1"

import unittest
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    """Tests the ChequingAccountClass."""

    def setUp(self) -> None:
        self.account_number = 1234
        self.client_number = 1
        self.balance = 1000.0
        self.date_created = date(2024, 1, 1)
        self.overdraft_limit = -100
        self.overdraft_rate = 0.05

        self.bank_account = ChequingAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.overdraft_limit,
            self.overdraft_rate
            )

    def test_init_object_initialized_to_correct_state(self):
        # Assert
        # Superclass private attributes
        self.assertEqual(self.account_number, 
                         self.bank_account._BankAccount__account_number)
        self.assertEqual(self.client_number, self.bank_account._BankAccount__client_number)
        self.assertEqual(self.balance, self.bank_account._BankAccount__balance)
        
        # Superclass protected attribute 
        self.assertEqual(self.date_created, self.bank_account._date_created)

        # Subclass private attributes
        self.assertEqual(self.overdraft_limit, 
                         self.bank_account._ChequingAccount__overdraft_limit)
        self.assertEqual(self.overdraft_rate, 
                         self.bank_account._ChequingAccount__overdraft_rate)
        
    def test_init_overdraft_limit_invalid_type_initialize_state(self):
        # Arrange
        self.overdraft_limit = "string"
        self.bank_account = ChequingAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.overdraft_limit,
            self.overdraft_rate
            )
        
        # Assert
        expected = -100
        actual = self.bank_account._ChequingAccount__overdraft_limit
        self.assertEqual(expected, actual)

    def test_init_overdraft_rate_invalid_type_initialize_state(self):
        # Arrange
        self.overdraft_rate = "string"

        # Act
        self.bank_account = ChequingAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.overdraft_limit,
            self.overdraft_rate
            )
        
        # Act
        expected = 0.05
        actual = self.bank_account._ChequingAccount__overdraft_rate
        self.assertEqual(expected, actual)

    def test_init_date_created_invalid_type_initialize_state(self):
        # Arrange
        self.date_created = "string"

        # Act
        self.bank_account = ChequingAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.overdraft_limit,
            self.overdraft_rate
            )
        
        # Assert
        expected = date.today()
        actual = self.bank_account._date_created
        self.assertEqual(expected, actual)

    def test_get_service_charges_default_when_balance_greater_than_limit(self):
        # Arrange
        self.bank_account._BankAccount__balance = 1000.00

        # Act
        expected = 0.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_default_when_balance_less_than_limit(self):
        # Arrange
        self.bank_account._BankAccount__balance = -150

        # Act
        expected = 3
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_default_when_balance_equal_to_limit(self):
        # Arrange     
        self.bank_account._BankAccount__balance = -100.00

        # Act
        expected = 0.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        # Act
        actual = self.bank_account.__str__()        

        # Assert
        expected = (f"Account Number: 1234 Balance: $1,000.00\n"
                    "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing")
        self.assertEqual(expected, actual)


        