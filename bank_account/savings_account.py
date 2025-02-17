"""This module defines the SavingsAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Represents a savings account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """Initializes a new instance of the SavingsAccount class.

        Args:
            SERVICE_CHARGE_PREMIUM(float): A constant value representing
                additional charges placed when a savings account goes
                below the minimum_balance.
            account_number(int): An integer value representing the
                savings account number
            client_number(int): An integer value representing
                the client number.
            balance(float): A float value representing the current
                balance of the savings account.
            date_created(date): The date the savings account was
                created.
            minimum_balance(float): The minimum value a balance can be 
                before further service charges are applied.


        Raises:
            ValueError: Raised when the account_number or client_number
                argument values are not an integer type, or when the
                balance argument value cannot be converted to a float.
        """

        super().__init__(0.5, account_number, client_number, balance, 
                         date_created)
        
        self.SERVICE_CHARGE_PREMIUM = 2.0
        
        self.__minimum_balance = minimum_balance