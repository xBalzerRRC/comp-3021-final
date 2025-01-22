"""This module defines the Client class."""

__author__ = "Xavier Balzer"
__version__= "1.2.1"

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
                
    @property
    def client_number(self) -> int:
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        return self.__email_address
        
