#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method for defining the sound an animal makes."""
        pass


class Dog(Animal):
    """Dog class inherits from Animal."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inherits from Animal."""
    def sound(self):
        return "Meaow"
