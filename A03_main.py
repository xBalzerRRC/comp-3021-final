"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Xavier Balzer"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client





# 2. Create a Client object with data of your choice.
client = Client(1234, "Xavier", "Balzer", "xbalzer@rrc.ca")



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

chequing_account = ChequingAccount(2222, 1234, 100000, date.today(), 100, 0.05)
savings_account = SavingsAccount(1111, 1234, 200000, date.today(), 1000)



# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

ChequingAccount.attach(chequing_account, client)
SavingsAccount.attach(savings_account, client)



# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

client2 = Client(4321, "John", "Doe", "jdoe@rrc.ca")
savings2 = SavingsAccount(9999, 4321, 100000, date.today(), 100)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_account.withdraw(2000.0)
    savings_account.withdraw(3000.0)
    chequing_account.deposit(100000.0)
    savings_account.deposit(100000.0)
except ValueError as e:
        print (e)

try:
    chequing_account.withdraw(50.0)
    savings_account.withdraw(50.0)
    chequing_account.deposit(100.0)
    savings_account.deposit(100.0)
except ValueError as e:
        print (e)

try:
    savings2.withdraw(3000.0)
    savings2.deposit(100000.0)
except ValueError as e:
        print (e)

try:
    savings2.withdraw(100.0)
    savings2.deposit(500.0)
except ValueError as e:
        print (e)