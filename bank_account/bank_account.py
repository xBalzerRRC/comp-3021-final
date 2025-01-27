"""This module defines the BankAccount class."""

__author__ = "Xavier Balzer"
__version__= "1.3.2"

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

    @property
    def account_number(self) -> int:
        """Gets the bank account number.
        
        Returns:
            int: The bank account number.
        """

        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """Gets the client number.
        
        Returns:
            int: The client number.
        """

        return self.__client_number
    
    @property
    def balance(self) -> float:
        """Gets the balance of the bank account.
        
        Returns:
            float: The balance of the bank account.
        """

        return self.__balance
    
    def update_balance(self, amount: float):
        """Updates the balance if the amount attribute value can be
        successfully converted to a float.

        Args:
            amount(float): Amount of currency received.
        """

        if isinstance(amount, float):
            self.__balance += amount

    def deposit(self, amount: float):
        """Passes the amount attribute value to the update_balance
            method.
        
        Args:
            amount(float): Amount of currency received.

        Raises:
            ValueError: Raised when amount received is non-numeric
                or not positive.
        """

        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        elif amount < 0:
            raise ValueError(f"Deposit amount: {amount:,.2f} must be positive.")
        
        else: 
            self.update_balance(amount)

    def withdraw(self, amount: float):
        """Passes negative amount attribute value
            to the update_balance method.
        
        Args:
            amount(float): Amount of currency received.

        Raises:
            ValueError: Raised when amount received is non-numeric, 
                not positive, or larger than the account balance. 
        """

        if not isinstance(amount, float):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
        
        elif amount < 0:
            raise ValueError(f"Withdrawal amount: {amount:,.2f} must be positive.")
        
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}.")
        else:
            amount = -abs(amount)
            self.update_balance(amount)

    def __str__(self) -> str:
        """Returns a string representation of the BankAccount object's
            balance and account number attributes.

        Returns:
            str: A string representation of the BankAccount object's 
            balance and account number attributes.
        """

        string_representation = ( 
            f"Account Number: {self.account_number} "
            f"Balance: ${self.balance:,.2f}\n"
        )

        return string_representation

