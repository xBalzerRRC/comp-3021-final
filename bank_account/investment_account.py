"""This module defines the InvestmentAccount class."""

__author__ = "Xavier Balzer"
__version__ = "1.2.4"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

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
        
        try:
            management_fee = float(management_fee)

        except ValueError:
            management_fee = 2.55
        
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self._management_fee = management_fee

        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """
        if self._date_created >= self.TEN_YEARS_AGO:
            return super().__str__() + (f"\nDate Created: {self._date_created} "
                                        f"Management Fee: ${self._management_fee:,.2f} "
                                        "Account Type: Investment")
        else:
            return super().__str__() + (f"\nDate Created: {self._date_created} "
                                        "Management Fee: Waived "
                                        "Account Type: Investment")
        
    def get_service_charges(self) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """ 
    
        service_charges = self.__strategy.calculate_service_charges(self)

        return service_charges

        
        