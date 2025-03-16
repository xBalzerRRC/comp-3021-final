"""This module defines the ManagementFeeStrategy subclass."""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """Represents a service charge strategy that 
    """
    def __init__(self, date_created: date, management_fee: float):
        """Initializes a new instance of the ManagementFeeStrategy 
        subclass.
        
        Args:
            date_created(date): The date the investment account was
                created.
            management_fee(float): The management fee for an investment
                account.
        """

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        if self.TEN_YEARS_AGO < self.__date_created:
            service_charge += self.__management_fee

        return service_charge
                