"""This module defines the SavingsAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.2.2"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """Represents a savings account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """Initializes a new instance of the SavingsAccount class.

        Args:
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

        super().__init__(account_number, client_number, balance, 
                         date_created)
        
        try:
            minimum_balance = float(minimum_balance)

        except ValueError:
            minimum_balance = 50       

        self.__minimum_balance = minimum_balance
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

    def __str__(self):
        """Returns a string representation of the BankAccount object's
            balance and account number attributes.

        Returns:
            str: A string representation of the BankAccount object's 
            balance and account number attributes.
        """

        return super().__str__() + (f"\nMinimum Balance: "
                                    f"${self.__minimum_balance:,.2f} "
                                    "Account Type: Savings")
    
    def get_service_charges(self) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """

        service_charges = self.__strategy.calculate_service_charges(self)

        return service_charges