"""This module defines the BankAccount class."""

__author__ = "Xavier Balzer"
__version__= "1.0.0"

class BankAccount:
    """Represents a bank account within a banking system."""

    def __init__(self, account_number: int, client_number: int, balance: float):
        """Initializes a new instance of the BankAccount class.

        Args:
            account_number(int): An integer value representing the bank
                account number
            client_number(int): An integer value representing
                the client number.
            balance(float): A float value representing the current
                balance of the bank account.

        Raises:

        """

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance