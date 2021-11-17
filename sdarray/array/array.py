# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Coordof, Data


# submodules
from . import coords
from . import dims
from .dims import time, chan
from .mixins import KeywordOnly


# dataclasses
@dataclass
class Array(AsDataArray, KeywordOnly):
    """Common single-dish data structure."""

    data: Data[Tuple[time, chan], Any]
    """Time-vs-channel (two-dimensional) data."""

    time: Coordof[dims.Time] = "2000-01-01"
    """Start time in UTC."""

    chan: Coordof[dims.Chan] = 0
    """Channel number."""

    scan: Coordof[coords.Scan] = "0"
    """Scan label."""

    mode: Coordof[coords.Mode] = "0"
    """Mode label."""

    beam: Coordof[coords.Beam] = "0"
    """Beam label."""

    spw: Coordof[coords.SpW] = "0"
    """Spectral window label."""

    pol: Coordof[coords.Pol] = "0"
    """Polarization label."""