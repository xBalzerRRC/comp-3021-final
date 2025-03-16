"""This module defines the ChequingAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.5.3"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """Represents a chequing account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float,
                 overdraft_rate: float):
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
                balance, overdraft_limit, or overdraft_rate argument 
                values cannot be converted to a float.
        """

        super().__init__(account_number, client_number, balance, 
                         date_created)
        
        try:
            overdraft_limit = float(overdraft_limit)

        except ValueError:
            overdraft_limit = -100

        try:
            overdraft_rate = float(overdraft_rate)

        except ValueError:
            overdraft_rate = 0.05

        # Private attributes
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """
        
        return super().__str__() + (f"\nOverdraft Limit: "
            f"${self.__overdraft_limit:,.2f} Overdraft Rate: "
            f"{self.__overdraft_rate:.2%} Account Type: Chequing")

    def get_service_charges(self) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """      

        service_charges = self.__strategy.calculate_service_charges(self)

        return service_charges
