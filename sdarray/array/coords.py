# standard library
from dataclasses import dataclass
from typing import Tuple


# dependencies
import numpy as np
from xarray_dataclasses import Attr, Data


# submodules
from . import dims


# dataclasses (time-chan data)
@dataclass
class Mask:
    """Mask of array data."""

    data: Data[Tuple[dims.time, dims.chan], np.bool_]
    long_name: Attr[str] = "Mask for array data"
    short_name: Attr[str] = "mask"


@dataclass
class Sigma:
    """Uncertainty of array data."""

    data: Data[Tuple[dims.time, dims.chan], np.float64]
    long_name: Attr[str] = "Uncertainty of array data"
    short_name: Attr[str] = "sigma"


@dataclass
class Weight:
    """Weight of array data."""

    data: Data[Tuple[dims.time, dims.chan], np.float64]
    long_name: Attr[str] = "Weight for array data"
    short_name: Attr[str] = "weight"


# dataclasses (time labels)
@dataclass
class Scan:
    """Scan label."""

    data: Data[dims.time, np.str_]
    long_name: Attr[str] = "Scan label"
    short_name: Attr[str] = "scan"


@dataclass
class Mode:
    """Mode label."""

    data: Data[dims.time, np.str_]
    long_name: Attr[str] = "Mode label"
    short_name: Attr[str] = "mode"


# dataclasses (time data)
@dataclass
class Exposure:
    """Exposure time."""

    data: Data[dims.time, np.float64]
    long_name: Attr[str] = "Exposure time"
    short_name: Attr[str] = "exposure"
    units: Attr[str] = "s"


@dataclass
class Interval:
    """Interval time."""

    data: Data[dims.time, np.float64]
    long_name: Attr[str] = "Interval time"
    short_name: Attr[str] = "interval"
    units: Attr[str] = "s"


@dataclass
class Longitude:
    """Sky longitude."""

    data: Data[dims.time, np.float64]
    long_name: Attr[str] = "Sky longitude" ""
    short_name: Attr[str] = "longitude"
    units: Attr[str] = "deg"


@dataclass
class Latitude:
    """Sky latitude."""

    data: Data[dims.time, np.float64]
    long_name: Attr[str] = "Sky latitude"
    short_name: Attr[str] = "latitude"
    units: Attr[str] = "deg"


# dataclasses (chan labels)
@dataclass
class Beam:
    """Beam label."""

    data: Data[dims.chan, np.str_]
    long_name: Attr[str] = "Beam label"
    short_name: Attr[str] = "beam"


@dataclass
class SpW:
    """Spectral window label."""

    data: Data[dims.chan, np.str_]
    long_name: Attr[str] = "Spectral window label"
    short_name: Attr[str] = "spw"


@dataclass
class Pol:
    """Polarization label."""

    data: Data[dims.chan, np.str_]
    long_name: Attr[str] = "Polarization label"
    short_name: Attr[str] = "pol"


# dataclasses (chan data)
@dataclass
class LonOffset:
    """Offset from sky longitude."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Offset from sky longitude"
    short_name: Attr[str] = "lon_offset"
    units: Attr[str] = "deg"


@dataclass
class LatOffset:
    """Offset from sky latitude."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Offset from sky latitude"
    short_name: Attr[str] = "lat_offset"
    units: Attr[str] = "deg"


@dataclass
class CenterFreq:
    """Center frequency."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Center frequency"
    short_name: Attr[str] = "center_freq"
    units: Attr[str] = "Hz"


@dataclass
class RefFreq:
    """Reference frequency."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Reference frequency"
    short_name: Attr[str] = "ref_freq"
    units: Attr[str] = "Hz"


@dataclass
class Resolution:
    """Spectral resolution."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Spectral resolution"
    short_name: Attr[str] = "resolution"
    units: Attr[str] = "Hz"


@dataclass
class Width:
    """Channel width."""

    data: Data[dims.chan, np.float64]
    long_name: Attr[str] = "Channel width"
    short_name: Attr[str] = "width"
    units: Attr[str] = "Hz"
