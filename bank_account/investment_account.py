"""This module defines the InvestmentAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """Represents a investment account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """Initializes a new instance of the InvestmentAccount class.

        Args:
            account_number(int): An integer value representing the
                investment account number
            client_number(int): An integer value representing
                the client number.
            balance(float): A float value representing the current
                balance of the investment account.
            date_created(date): The date the investment account was
                created.
            management_fee(float): The management fee for an investment
                account.


        Raises:
            ValueError: Raised when the account_number or client_number
                argument values are not an integer type, or when the
                balance argument value cannot be converted to a float.
        """

        super().__init__(account_number, client_number, balance, 
                         date_created)
        
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self.__management_fee - management_fee

        