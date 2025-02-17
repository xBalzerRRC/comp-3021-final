"""This module defines the SavingsAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

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
        
        try:
            minimum_balance = float(minimum_balance)

        except ValueError:
            minimum_balance = 50       

        self.SERVICE_CHARGE_PREMIUM = 2.0

        self.__minimum_balance = minimum_balance

    def __str__(self):
        """Returns a string representation of the BankAccount object's
            balance and account number attributes.

        Returns:
            str: A string representation of the BankAccount object's 
            balance and account number attributes.
        """

        return super().__str__() + (f"\nMinimum Balance:"
                                    f"{self.__minimum_balance:,.2f}"
                                    "Account Type: Savings")
    

    def get_service_charges(self) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """

        if self.balance >= self.__minimum_balance:
            service_charges = self.BASE_SERVICE_CHARGE
        
        else:
            service_charges = (self.BASE_SERVICE_CHARGE *
                               self.SERVICE_CHARGE_PREMIUM)
        
        return service_charges

    