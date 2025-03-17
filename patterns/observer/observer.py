"""This module defines the Observer superclass."""

__author__ = "Xavier Balzer"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """Used to maintain all possible ways that 
    service charges can be applied to accounts.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        pass