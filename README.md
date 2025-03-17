# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Xavier Balzer

## Assignment

Assignment #1 - Classes: This assignment will produce some foundational classes to be used in an overall system. The classes will incorporate the outcomes associated with Module 01. Specifically, these classes will incorporate encapsulation through the use of private attributes and public accessors and mutators. Additionally, these classes will benefit from thorough unit testing, including unit test planning.

Assignment #2 - Abstraction, Inheritance and Polymorphism: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

Assignment #3 - Design Patterns: This assignment will address issues associated with the scalability and maintainability of the current service charge calculation functionality. In this assignment the Strategy Pattern will be applied to simplify and add scalability to the service charge functionality. In addition, the Observer Pattern will be introduced. Using the Observer Pattern a client will be notified whenever a large transaction takes place and/or whenever an account balance drops below a minimum value.

## Encapsulation

By making use of accessors and mutators for the BankAccount class' attributes, we are able to read and assign values to private attributes without needing direct access to them. For instance, methods such as update_balance, withdraw, and deposit enable us to make changes to the balance class attribute without needing to modify the variable directly.

## Polymorphism

I achieved polymorphism in the BankAccount subclass via the use of the get_service_charges method, which allowed us to calculate the price of a bank account's service charges depending on what kind of bank account was being used, the use of super() with __init__ and __str__ class methods throughout the subclasses also allowed for BankAccount class attributes and string representations to be inherited throughout all the subclasses.

## Strategy Pattern

In this file the Strategy Pattern is employed to avoid the use of repetitive code when processing service charges across different banking account modules. Calling a strategy pattern that uses a method instead of invoking the method itself allows us to reuse the same code across multiple different classes without needing to write it individually for each one.
