"""This module defines the ChequingAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """Represents a chequing account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """Initializes a new instance of the ChequingAccount class.

        Args:
            account_number(int): An integer value representing the
                chequing account number
            client_number(int): An integer value representing
                the client number.
            balance(float): A float value representing the current
                balance of the chequing account.
            date_created(date): The date the chequing account was
                created.
            overdraft_limit(float): The maximum amount a balance can be
                overdrawn (below 0.00) before overdraft fees are 
                applied.
            overdraft_rate(float): The rate to which overdraft fees will
                be applied.

        Raises:
            ValueError: Raised when the account_number or client_number
                argument values are not an integer type, or when the
                balance argument value cannot be converted to a float.
        """

        # Private attributes
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate