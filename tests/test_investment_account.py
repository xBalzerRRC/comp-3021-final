"""This module defines the TestInvestmentAccount class.

Example:
    $ python -m unittest tests/test_investment_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.1.1"

import unittest
from bank_account.bank_account import BankAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):
    """Tests the InvestmentAccountClass."""

    def setUp(self) -> None:
        self.account_number = 1234
        self.client_number = 1
        self.balance = 1000.0
        self.date_created = date(2024, 1, 1)
        self.management_fee = 3.00

        self.bank_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
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

        # Subclass protected attributes
        self.assertEqual(self.management_fee, 
                         self.bank_account._management_fee)
        
    def test_init_object_initialized_correct_state_invalid_manager_fee(self):
        # Arrange
        self.management_fee = "string"
        self.bank_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
            )
        # Act
        expected = 2.55
        actual = self.bank_account._management_fee

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_date_created_over_ten_years(self):
        # Arrange
        self.date_created = date(2000, 1, 1)

        self.bank_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
            )
        
        # Act
        expected = 0.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_date_created_exactly_ten_years(self):
        # Arrange
        self.date_created = date.today() - timedelta(days = 10 * 365.25)

        # Act
        expected = 3.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_get_service_charges_date_created_under_ten_years(self):
        # Arrange
        self.date_created = date(2025, 1, 1)

        # Act
        expected = 3.5
        actual = self.bank_account.get_service_charges()

        # Assert
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation_date_over_ten_years(self):
        # Act
        self.date_created = date(2015, 1, 1)

        self.bank_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
            )

        actual = self.bank_account.__str__()        

        # Assert
        expected = (f"Account Number: 1234 Balance: $1,000.00\n"
                    "Date Created: 2015-01-01 Management Fee: Waived " 
                    "Account Type: Investment")
        
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation_date_under_ten_years(self):
        # Act
        self.date_created = date(2025, 1, 1)

        self.bank_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
            )

        actual = self.bank_account.__str__()        

        # Assert
        expected = (f"Account Number: 1234 Balance: $1,000.00\n"
                    "Date Created: 2025-01-01 Management Fee: $3.00 " 
                    "Account Type: Investment")
        self.assertEqual(expected, actual)
    
    
    
    
    
    
    
    
