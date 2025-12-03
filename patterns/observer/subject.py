"""This module defines the Subject class."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """Represents a class responsible for maintaining a list of its 
    observers and notifying them of state changes and events."""

    def __init__(self) -> None:
        """Initializes a new instance of the Subject class."""

        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer):
        """Adds a new observer to the subject's list of observers.
        
        Args:
            observer (Observer): The observer instance that should be 
            notified of state changes.
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """Removes an observer from the subject's list of observers.
        
        Args:
            observer (Observer): The observer instance to remove."""

        pass

    @abstractmethod
    def notify(self, observer: Observer):
        """Alerts all registered observers of a state change by 
           sending a message.

        Args:
            observer (Observer): The observer instance that will be
            alerted.
        """
        
        pass

