"""This module defines the TestBankAccount class.

Example:
    $ python -m unittest tests/test_bank_account.py
"""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Tests for the BankAccount class."""

    def setUp(self):
        account_number = 1234
        client_number = 1
        balance = 1000.0

        self.bankaccount = BankAccount(account_number, client_number, balance)
        