__all__ = [
    "Scan",
    "Mode",
    "Exposure",
    "Interval",
    "RightAscension",
    "Declination",
]


# standard library
from dataclasses import dataclass


# dependencies
import numpy as np
from xarray_dataclasses import Attr, Data


# submodules
from .dims import time, chan


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


# dataclasses (time observables)
@dataclass
class Exposure:
    """Exposure time."""

    data: Data[time, np.str_]
    long_name: Attr[str] = "Exposure time"
    short_name: Attr[str] = "exposure"
    units: Attr[str] = "s"


@dataclass
class Interval:
    """Interval time."""

    data: Data[time, np.str_]
    long_name: Attr[str] = "Interval time"
    short_name: Attr[str] = "interval"
    units: Attr[str] = "s"


@dataclass
class RightAscension:
    """Right ascension."""

    data: Data[time, np.float64]
    long_name: Attr[str] = "Right ascension"
    short_name: Attr[str] = "ra"
    units: Attr[str] = "deg"


@dataclass
class Declination:
    """Declination."""

    data: Data[time, np.float64]
    long_name: Attr[str] = "Declination"
    short_name: Attr[str] = "dec"
    units: Attr[str] = "deg"

