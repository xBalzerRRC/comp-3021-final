# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Xavier Balzer

## Assignment

Assignment #1 - Classes: This assignment will produce some foundational classes to be used in an overall system. The classes will incorporate the outcomes associated with Module 01. Specifically, these classes will incorporate encapsulation through the use of private attributes and public accessors and mutators. Additionally, these classes will benefit from thorough unit testing, including unit test planning.

Assignment #2 - Abstraction, Inheritance and Polymorphism: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

## Encapsulation

By making use of accessors and mutators for the BankAccount class' attributes, we are able to read and assign values to private attributes without needing direct access to them. For instance, methods such as update_balance, withdraw, and deposit enable us to make changes to the balance class attribute without needing to modify the variable directly.
