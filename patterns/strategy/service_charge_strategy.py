"""This module defines the ServiceChargeStrategy superclass."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """Used to maintain all possible ways that 
    service charges can be applied to accounts.
    """
    
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        pass