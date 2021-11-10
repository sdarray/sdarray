__all__ = ["Scan", "Mode"]


# standard library
from dataclasses import dataclass


# dependencies
import numpy as np
from xarray_dataclasses import Attr, Data


# submodules
from .dims import time


# dataclasses (time labels)
@dataclass
class Scan:
    """Scan label."""

    data: Data[time, np.str_]
    long_name: Attr[str] = "Scan label"
    short_name: Attr[str] = "scan"


@dataclass
class Mode:
    """Mode label."""

    data: Data[time, np.str_]
    long_name: Attr[str] = "Mode label"
    short_name: Attr[str] = "mode"
