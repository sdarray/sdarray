# dependencies
import numpy as np
import sdarray as sd
from xarray_dataclasses import asdataarray


# test functions
def test_scan() -> None:
    data = np.array(["0"], np.str_)
    time = asdataarray(sd.coords.Scan(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_mode() -> None:
    data = np.array(["0"], np.str_)
    time = asdataarray(sd.coords.Mode(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_exposure() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.Exposure(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_interval() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.Interval(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_ra() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.RA(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_dec() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.Dec(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_beam() -> None:
    data = np.array(["0"], np.str_)
    time = asdataarray(sd.coords.Beam(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_spw() -> None:
    data = np.array(["0"], np.str_)
    time = asdataarray(sd.coords.SpW(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_pol() -> None:
    data = np.array(["0"], np.str_)
    time = asdataarray(sd.coords.Pol(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_center_freq() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.CenterFreq(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_ref_freq() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.RefFreq(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_resolution() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.Resolution(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type


def test_width() -> None:
    data = np.array([0.0], np.float64)
    time = asdataarray(sd.coords.Width(data))

    assert time.data == data
    assert time.dims == ("chan",)
    assert time.dtype.type == data.dtype.type
