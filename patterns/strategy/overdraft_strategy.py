"""This module defines the OverdraftStrategy subclass."""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """Represents a service charge strategy within a banking system."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """Initializes a new instance of the OverdraftStrategy subclass.
        
        Args:
            overdraft_limit(float): The maximum amount a balance can be
                overdrawn (below 0.00) before overdraft fees are 
                applied.
            overdraft_rate(float): The rate to which overdraft fees will
                be applied. 
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """
        
        service_charges = self.BASE_SERVICE_CHARGE
        
        if account.balance < self.__overdraft_limit:
            service_charges +=  ((self.__overdraft_limit - account.balance) * 
                                 self.__overdraft_rate)
        
        return service_charges