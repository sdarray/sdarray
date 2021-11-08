__all__ = ["Time", "Chan", "time", "chan"]


# standard library
from dataclasses import dataclass


# dependencies
from typing_extensions import Literal
from xarray_dataclasses import Attr, Data


# constants
time = Literal["time"]
chan = Literal["chan"]


# dataclasses
@dataclass
class Time:
    """Time in UTC."""

    data: Data[time, Literal["M8[ns]"]]
    long_name: Attr[str] = "Time in UTC"
    short_name: Attr[str] = "time"


@dataclass
class Chan:
    """Channel ID."""

    data: Data[chan, Literal["i8"]]
    long_name: Attr[str] = "Channel ID"
    short_name: Attr[str] = "chan"
