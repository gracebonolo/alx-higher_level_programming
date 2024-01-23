#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is a private instance attribute.
        """
        self.__size = size
