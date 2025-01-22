"""This module defines the Client class."""

__author__ = "Xavier Balzer"
__version__= "1.0.0"

from email_validator.exceptions_types import EmailNotValidError
from email_validator.validate_email import validate_email

class Client:
    
    def __init__(self, client_number: int, first_name: str, 
                 last_name: str, email_address: str):
        
        first_name = first_name.strip()
        last_name = last_name.strip()
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be numeric.")
        
        if len(first_name) == 0:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name) == 0:
            raise ValueError("Last name cannot be blank.")
        
        try: 
            validate_email(email_address)

        except EmailNotValidError:
            email_address = "email@pixell-river.com"

        

        
