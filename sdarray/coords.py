__all__ = [
    "Scan",
    "Mode",
    "Exposure",
    "Interval",
    "RightAscension",
    "Declination",
    "Beam",
    "SpectralWindow",
    "Polarization",
    "Frequency",
    "RefFrequency",
    "Resolution",
    "Width",
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


# dataclasses (chan labels)
@dataclass
class Beam:
    """Beam label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Beam label"
    short_name: Attr[str] = "beam"


@dataclass
class SpectralWindow:
    """Spectral window label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Spectral window label"
    short_name: Attr[str] = "spw"


@dataclass
class Polarization:
    """Polarization label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Polarization label"
    short_name: Attr[str] = "pol"


# dataclasses (chan observables)
@dataclass
class Frequency:
    """Center frequency."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Center frequency"
    short_name: Attr[str] = "freq"
    units: Attr[str] = "Hz"


@dataclass
class RefFrequency:
    """Reference frequency."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Reference frequency"
    short_name: Attr[str] = "ref_freq"
    units: Attr[str] = "Hz"


@dataclass
class Resolution:
    """Spectral resolution."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Spectral resolution"
    short_name: Attr[str] = "res"
    units: Attr[str] = "Hz"


@dataclass
class Width:
    """Channel width."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Channel width"
    short_name: Attr[str] = "width"
    units: Attr[str] = "Hz"
