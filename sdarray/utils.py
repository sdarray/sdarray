"""Submodule for the utilities."""


# standard library
from dataclasses import field
from typing import TypeVar


# type hints
T = TypeVar("T")


# runtime functions
def readonly(default: T) -> T:
    """Create a read-only field for dataclasses."""
    return field(default=default, init=False)
