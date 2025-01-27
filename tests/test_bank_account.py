"""This module defines the TestBankAccount class.

Example:
    $ python -m unittest tests/test_bank_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.4.1"

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

    def test_account_number_accessor_returns_correct_state(self):
        # Act
        actual = self.bankaccount._BankAccount__account_number

        # Assert
        expected = 1234
        self.assertEqual(expected, actual)

    def test_client_number_accessor_returns_correct_state(self):
        # Act
        actual = self.bankaccount._BankAccount__client_number

        # Assert
        expected = 1
        self.assertEqual(expected, actual)

    def test_balance_accessor_returns_correct_state(self):
        # Act
        actual = self.bankaccount._BankAccount__balance

        # Assert
        expected = 1000.0
        self.assertEqual(expected, actual)

    def test_update_balance_updates_correct_when_amount_positive(self):
        # Arrange
        account_number = 1234
        client_number = 1
        balance = 1000.0
        amount = 10.0

        # Act
        self.bankaccount = BankAccount(account_number, client_number, balance)
        self.bankaccount.update_balance(amount)
        # Assert 
        expected = 1010.00
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_update_balance_updates_correct_when_amount_negative(self):
        # Arrange
        amount = -10.0

        # Act
        self.bankaccount.update_balance(amount)
        # Assert 
        expected = 990.00
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_update_balance_unchanged_when_amount_invalid(self):
        # Arrange
        amount = "10"

        # Act
        self.bankaccount.update_balance(amount)
        # Assert 
        expected = 1000.00
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_deposit_updates_balance_correctly_when_valid_amount(self):
        # Arrange
        amount = 10.0

        # Act
        self.bankaccount.deposit(amount)
        # Assert 
        expected = 1010.00
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_deposit_negative_amount_raises_value_error(self):
        # Arrange
        amount = -10.0

        # Act
        with self.assertRaises(ValueError) as context:
            self.bankaccount.deposit(amount)
        # Assert 
        expected = "Deposit amount: -10.00 must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_updates_balance_correctly_when_valid_amount(self):
        # Arrange
        amount = 10.0

        # Act
        self.bankaccount.withdraw(amount)
        # Assert 
        expected = 990.00
        actual = self.bankaccount._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_withdraw_negative_amount_raises_value_error(self):
        # Arrange
        amount = -10.0

        # Act
        with self.assertRaises(ValueError) as context:
            self.bankaccount.withdraw(amount)
        # Assert 
        expected = "Withdrawal amount: -10.00 must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_excessive_amount_raises_value_error(self):
        # Arrange
        amount = 2000.0

        # Act
        with self.assertRaises(ValueError) as context:
            self.bankaccount.withdraw(amount)
        # Assert 
        expected = "Withdrawal amount: $2,000.00 must not exceed the account balance: $1,000.00."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        # Act
        actual = self.bankaccount.__str__()        

        # Assert
        expected = f"Account Number: 1234 Balance: $1,000.00\n"
        self.assertEqual(expected, actual)
