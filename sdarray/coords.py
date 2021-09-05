"""Submodule for the definitions of the sdarray coordinates."""


# standard library
from dataclasses import dataclass


# dependencies
from typing_extensions import Literal
from xarray_dataclasses import Attr, Data


# submodules
from .utils import readonly, unwrap


# type hints
Ti = Literal["t"]
Ch = Literal["ch"]
DT64 = Literal["datetime64[ns]"]


# dataclasses (dims)
@dataclass
class Time:
    """Observed time."""

    data: Data[Ti, DT64]
    doc: Attr[str] = readonly(unwrap(__doc__))
    long_name: Attr[str] = readonly("Observed time")


@dataclass
class Channel:
    """Channel number."""

    data: Data[Ch, int]
    doc: Attr[str] = readonly(unwrap(__doc__))
    long_name: Attr[str] = readonly("Channel number")

