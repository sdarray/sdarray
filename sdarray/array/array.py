# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Coordof, Data
from xarray_dataclasses.typing import Coord


# submodules
from . import coords
from . import dims
from .dims import time, chan
from .utils import KeywordOnly


# dataclasses
@dataclass
class Array(AsDataArray, KeywordOnly):
    """Common single-dish data structure."""

    data: Data[Tuple[time, chan], Any]
    """Two-dimensional array data."""

    mask: Coordof[coords.Mask] = False
    """Mask of array data."""

    sigma: Coordof[coords.Sigma] = 0.0
    """Uncertainty of array data."""

    weight: Coordof[coords.Weight] = 1.0
    """Weight of array data."""

    time: Coordof[dims.Time] = "2000-01-01"
    """Start time in UTC."""

    scan: Coordof[coords.Scan] = "0"
    """Scan label."""

    mode: Coordof[coords.Mode] = "0"
    """Mode label."""

    exposure: Coordof[coords.Exposure] = 0.0
    """Exposure time."""

    interval: Coordof[coords.Interval] = 0.0
    """Interval time."""

    longitude: Coordof[coords.Longitude] = 0.0
    """Sky longitude."""

    latitude: Coordof[coords.Latitude] = 0.0
    """Sky latitude."""

    chan: Coordof[dims.Chan] = 0
    """Channel number."""

    beam: Coordof[coords.Beam] = "0"
    """Beam label."""

    spw: Coordof[coords.SpW] = "0"
    """Spectral window label."""

    pol: Coordof[coords.Pol] = "0"
    """Polarization label."""

    lon_offset: Coordof[coords.LonOffset] = 0.0
    """Offset from sky longitude."""

    lat_offset: Coordof[coords.LatOffset] = 0.0
    """Offset from sky latitude."""

    center_freq: Coordof[coords.CenterFreq] = 0.0
    """Center frequency."""

    ref_freq: Coordof[coords.RefFreq] = 0.0
    """Reference frequency."""

    resolution: Coordof[coords.Resolution] = 0.0
    """Spectral resolution."""

    width: Coordof[coords.Width] = 0.0
    """Channel width."""
