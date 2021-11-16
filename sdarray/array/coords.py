# standard library
from dataclasses import dataclass
from typing import Tuple


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

    data: Data[time, np.float64]
    long_name: Attr[str] = "Exposure time"
    short_name: Attr[str] = "exposure"
    units: Attr[str] = "s"


@dataclass
class Interval:
    """Interval time."""

    data: Data[time, np.float64]
    long_name: Attr[str] = "Interval time"
    short_name: Attr[str] = "interval"
    units: Attr[str] = "s"


@dataclass
class Longitude:
    """Sky longitude."""

    data: Data[time, np.float64]
    long_name: Attr[str] = "Sky longitude" ""
    short_name: Attr[str] = "longitude"
    units: Attr[str] = "deg"


@dataclass
class Latitude:
    """Sky latitude."""

    data: Data[time, np.float64]
    long_name: Attr[str] = "Sky latitude"
    short_name: Attr[str] = "latitude"
    units: Attr[str] = "deg"


# dataclasses (chan labels)
@dataclass
class Beam:
    """Beam label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Beam label"
    short_name: Attr[str] = "beam"


@dataclass
class SpW:
    """Spectral window label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Spectral window label"
    short_name: Attr[str] = "spw"


@dataclass
class Pol:
    """Polarization label."""

    data: Data[chan, np.str_]
    long_name: Attr[str] = "Polarization label"
    short_name: Attr[str] = "pol"


# dataclasses (chan observables)
@dataclass
class CenterFreq:
    """Center frequency."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Center frequency"
    short_name: Attr[str] = "center_freq"
    units: Attr[str] = "Hz"


@dataclass
class RefFreq:
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
    short_name: Attr[str] = "resolution"
    units: Attr[str] = "Hz"


@dataclass
class Width:
    """Channel width."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Channel width"
    short_name: Attr[str] = "width"
    units: Attr[str] = "Hz"


@dataclass
class LonOffset:
    """Offset from sky longitude."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Offset from sky longitude"
    short_name: Attr[str] = "lon_offset"
    units: Attr[str] = "deg"


@dataclass
class LatOffset:
    """Offset from sky latitude."""

    data: Data[chan, np.float64]
    long_name: Attr[str] = "Offset from sky latitude"
    short_name: Attr[str] = "lat_offset"
    units: Attr[str] = "deg"


# dataclasses (time-chan observables)
@dataclass
class Mask:
    """Mask for an array."""

    data: Data[Tuple[time, chan], np.bool_]
    long_name: Attr[str] = "Mask for an array"
    short_name: Attr[str] = "mask"


@dataclass
class Sigma:
    """Uncertainty of an array."""

    data: Data[Tuple[time, chan], np.float64]
    long_name: Attr[str] = "Uncertainty of an array"
    short_name: Attr[str] = "sigma"


@dataclass
class Weight:
    """Weight for an array."""

    data: Data[Tuple[time, chan], np.float64]
    long_name: Attr[str] = "Weight for an array"
    short_name: Attr[str] = "weight"
