"""This module defines the Client class."""

__author__ = "Xavier Balzer"
__version__= "1.1.1"

from email_validator import validate_email, EmailNotValidError

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
            validated_email = validate_email(email_address, 
                                             check_deliverability = False)
            
            email_address = validated_email 

        except EmailNotValidError:
            email_address = "email@pixell-river.com"

        
        

        
