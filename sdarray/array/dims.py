__all__ = ["Time", "Chan", "time", "chan"]


# standard library
from dataclasses import dataclass


# dependencies
import numpy as np
from typing_extensions import Literal
from xarray_dataclasses import Attr, Data


# constants
time = Literal["time"]
"""Type hint for the time axis."""

chan = Literal["chan"]
"""Type hint for the channel axis."""


# dataclasses
@dataclass
class Time:
    """Start time in UTC."""

    data: Data[time, np.datetime64]
    long_name: Attr[str] = "Start time in UTC"
    short_name: Attr[str] = "time"


@dataclass
class Chan:
    """Channel number."""

    data: Data[chan, np.int64]
    long_name: Attr[str] = "Channel number"
    short_name: Attr[str] = "chan"
