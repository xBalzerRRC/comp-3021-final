"""This module defines the BankAccount class."""

__author__ = "Xavier Balzer"
__version__= "1.4.6"

from abc import ABC, abstractmethod
from datetime import datetime, date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer, update

class BankAccount(Subject, ABC):
    """Represents a bank account within a banking system."""

    def __init__(self, account_number: int, 
                 client_number: int, balance: float, date_created: date): 
        """Initializes a new instance of the BankAccount class.

        Args:
            BASE_SERVICE_CHARGE(float): A constant value representing
                base service charge.
            account_number(int): An integer value representing the bank
                account number
            client_number(int): An integer value representing
                the client number.
            balance(float): A float value representing the current
                balance of the bank account.
            date_created(date): The date the bank account was created.

        Raises:
            ValueError: Raised when the account_number or client_number
                argument values are not an integer type, or when the
                balance argument value cannot be converted to a float.
        """

        if not isinstance(account_number, int):
            raise ValueError("Account number must be numeric.")
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be numeric.")

        if not isinstance(date_created, date):
            date_created = date.today()

        try:
            balance = float(balance)

        except ValueError:
            balance = 0.0
        
        # Constants
        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        self.LOW_BALANCE_LEVEL = 50.0

        # Private attributes
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance

        # Protected attributes
        self._date_created = date_created

        super().__init__()

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
        """Updates balance with amount received.

        Args:
            amount(float): Amount of currency received.
        """

        if isinstance(amount, float):
            self.__balance += amount

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}: "
                        f"on account {self.__account_number}.")

        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction {amount}: "
                        f"on account {self.__account_number}.")


    def deposit(self, amount: float):
        """Deposits amount to balance.
        
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
        
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """Withdraws amount from balance.
        
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
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} " 
                             f"must not exceed the account balance: ${self.__balance:,.2f}.")
        
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
            f"Balance: ${self.balance:,.2f}"
        )

        return string_representation

    @abstractmethod
    def get_service_charges(self) -> float:
        """Returns the calculated service charges a BankAccount will 
            incur.

        Returns:
            float:  Calculated service charges.
        """      
        pass

    def attach(self, observer: Observer) -> None:
        """Adds a new observer to the Subject's list of observers."""

        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Removes an observer from the Subject's list of observers."""

        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Alerts all registered observers of a state change."""
        for observer in self._observers:
            Observer.update(observer, message)


    
