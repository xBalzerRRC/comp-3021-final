"""This module defines the BankAccount class."""

__author__ = "Xavier Balzer"
__version__= "1.1.0"

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
            ValueError: Raised when the account_number or client_number
                argument values are not an integer type, or when the
                balance argument value cannot be converted to a float.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be numeric.")
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be numeric.")

        try:
            balance = float(balance)

        except ValueError:
            balance = 0.0
            
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance