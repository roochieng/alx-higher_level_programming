#!/usr/bin/python3
"""Create a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __eq__(self, value):
        """Inverse. To give !="""
        return self.real != value

    def __ne__(self, value):
        """Inverse to give == """
        return self.real == value
