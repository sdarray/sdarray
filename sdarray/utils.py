"""Submodule for the utilities."""


# standard library
import re
from dataclasses import field
from typing import Optional, TypeVar


# constants
INDENT = re.compile(r"(\s{4})+")


# type hints
T = TypeVar("T")


# runtime functions
def readonly(default: T) -> T:
    """Create a read-only field for dataclasses."""
    return field(default=default, init=False)


def unwrap(doc: Optional[str]) -> str:
    """Unwrap a multi-line docstring."""
    if doc is None:
        return ""

    return " ".join(INDENT.sub("", doc).split())
