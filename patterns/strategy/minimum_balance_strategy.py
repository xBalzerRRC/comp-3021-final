"""This module defines the MinimumBalanceStrategy subclass."""

__author__ = "Xavier Balzer"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Represents a service charge strategy within a banking system."""
    
    def __init__(self, minimum_balance: float):
        """Initializes a new instance of the MinimumBalanceStrategy subclass.
        
        Args:
            minimum_balance(float): The minimum value a balance can be 
                before further service charges are applied.
        """

        self.SERVICE_CHARGE_PREMIUM = 2.0
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """
        
        service_charges = self.BASE_SERVICE_CHARGE

        if account.balance < self.__minimum_balance:
            service_charges *= self.SERVICE_CHARGE_PREMIUM
              
        return service_charges