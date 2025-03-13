"""This module defines the OverdraftStrategy subclass."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """Represents a service charge strategy within a banking system."""
