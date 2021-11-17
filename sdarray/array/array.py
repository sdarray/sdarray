# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Data


# submodules
from .dims import time, chan
from .mixins import KeywordOnly


# dataclasses
@dataclass
class Array(AsDataArray, KeywordOnly):
    """Common single-dish data structure."""

    data: Data[Tuple[time, chan], Any]
    """Time-vs-channel (two-dimensional) data."""
