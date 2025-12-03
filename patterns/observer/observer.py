"""This module defines the Observer superclass."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """Superclass used to define the interface for all concrete
    observers that need to be notified of changes in the subject.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """Notifies the observer of a state change in the subject.

        Args:
            message (str): The information or notification regarding the state change.
        """

        pass