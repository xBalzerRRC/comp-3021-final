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
    def attach(observer: Observer):
        pass

    @abstractmethod
    def detach(observer: Observer):
        pass

    @abstractmethod
    def notify(observer: Observer):
        pass

