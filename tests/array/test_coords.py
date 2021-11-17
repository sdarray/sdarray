# dependencies
import numpy as np
import sdarray as sd
from xarray_dataclasses import asdataarray


# constants
SHORT_NAME = "short_name"
UNITS = "units"


# test functions
def test_scan() -> None:
    data = np.array(["0"], np.str_)
    array = asdataarray(sd.array.coords.Scan(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "scan"


def test_mode() -> None:
    data = np.array(["0"], np.str_)
    array = asdataarray(sd.array.coords.Mode(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "mode"


def test_exposure() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Exposure(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "exposure"
    assert array.attrs[UNITS] == "s"


def test_interval() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Interval(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "interval"
    assert array.attrs[UNITS] == "s"


def test_longitude() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Longitude(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "longitude"
    assert array.attrs[UNITS] == "deg"


def test_latitude() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Latitude(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "latitude"
    assert array.attrs[UNITS] == "deg"


def test_beam() -> None:
    data = np.array(["0"], np.str_)
    array = asdataarray(sd.array.coords.Beam(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "beam"


def test_spw() -> None:
    data = np.array(["0"], np.str_)
    array = asdataarray(sd.array.coords.SpW(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "spw"


def test_pol() -> None:
    data = np.array(["0"], np.str_)
    array = asdataarray(sd.array.coords.Pol(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "pol"


def test_center_freq() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.CenterFreq(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "center_freq"
    assert array.attrs[UNITS] == "Hz"


def test_ref_freq() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.RefFreq(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "ref_freq"
    assert array.attrs[UNITS] == "Hz"


def test_resolution() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Resolution(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "resolution"
    assert array.attrs[UNITS] == "Hz"


def test_width() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.Width(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "width"
    assert array.attrs[UNITS] == "Hz"


def test_lon_offset() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.LonOffset(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "lon_offset"
    assert array.attrs[UNITS] == "deg"


def test_lat_offset() -> None:
    data = np.array([0.0], np.float64)
    array = asdataarray(sd.array.coords.LatOffset(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "lat_offset"
    assert array.attrs[UNITS] == "deg"


def test_mask() -> None:
    data = np.array([[False]], np.bool_)
    array = asdataarray(sd.array.coords.Mask(data))

    assert array.data == data
    assert array.dims == ("time", "chan")
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "mask"


def test_sigma() -> None:
    data = np.array([[0.0]], np.float64)
    array = asdataarray(sd.array.coords.Sigma(data))

    assert array.data == data
    assert array.dims == ("time", "chan")
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "sigma"


def test_weight() -> None:
    data = np.array([[1.0]], np.float64)
    array = asdataarray(sd.array.coords.Weight(data))

    assert array.data == data
    assert array.dims == ("time", "chan")
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "weight"
