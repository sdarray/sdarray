# standard library
from dataclasses import dataclass


# dependencies
import numpy as np
from typing_extensions import Literal
from xarray_dataclasses import Attr, Data


# type hints
time = Literal["time"]
"""Type hint of the time dimension."""

chan = Literal["chan"]
"""Type hint of the channel dimension."""


# dataclasses
@dataclass
class Time:
    """Start time in UTC."""

    data: Data[time, np.datetime64]
    long_name: Attr[str] = "Start time in UTC"
    short_name: Attr[str] = "time"


@dataclass
class Chan:
    """Generic channel."""

    data: Data[chan, np.int64]
    long_name: Attr[str] = "Generic channel"
    short_name: Attr[str] = "chan"
