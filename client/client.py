"""This module defines the Client class."""

__author__ = "Xavier Balzer"
__version__= "1.3.3"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime
import hashlib

class Client(Observer):
    """Represents a client's information within a banking system."""

    def __init__(self, client_number: int, first_name: str, 
                 last_name: str, email_address: str):
        """Initializes a new instance of the Client class.

        Args:
            client_number(int): An integer value representing
                the client number.
            first_name(str): The client's first name.
            last_name(str): The client's last name.
            email_address(str): The client's email address.
        
        Raises:
            ValueError: Raised when the client_number argument value is
                not an integer type, or when the first_name or last_name 
                argument values contain no non-whitespace characters.
            EmailNotValidError: Raised when an invalid email_address
                argument is evaluated by the validate_email method.
        """

        first_name = first_name.strip()
        last_name = last_name.strip()
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be numeric.")
        
        if len(first_name) == 0:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name) == 0:
            raise ValueError("Last name cannot be blank.")
        
        try: 
            validated_email = validate_email(email_address, 
                                             check_deliverability = False)
            email_address = validated_email.normalized

        except EmailNotValidError:
            email_address = "email@pixell-river.com"

        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
                
    @property
    def client_number(self) -> int:
        """Gets the client's client number.
        
        Returns:
            int: The client number of the client.
        """

        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """Gets the first name of the client.
        
        Returns:
            str: The first name of the client.
        """
        
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """Gets the last name of the client.
        
        Returns:
            str: The last name of the client.
        """

        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """Gets the email address of the client.
        
        Returns:
            str: The email address of the client.
        """

        return self.__email_address
        
    def __str__(self) -> str:
        """Returns a string representation of the Client object.

        Returns:
            str: A string representation of the Client object.
        """

        string_representation = ( 
            f"{self.last_name}, "
            f"{self.first_name} "
            f"[{self.client_number}] - "
            f"{self.email_address}\n"
        )

        return string_representation
    
    def update(self, message: str) -> None:
        """Sends a simulated email."""
        simulate_send_email(self.email_address, 
                            f"ALERT: Unusual Activity: {datetime.now()}", 
                            f"Notification for {self.client_number}: "
                            f"{self.first_name} {self.last_name}: {message}")
        
    def hash_password(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()