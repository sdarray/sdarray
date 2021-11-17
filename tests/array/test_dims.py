# dependencies
import numpy as np
import sdarray as sd
from xarray_dataclasses import asdataarray


# constants
SHORT_NAME = "short_name"


# test functions
def test_time() -> None:
    data = np.array(["2000-01-01"], np.datetime64)
    array = asdataarray(sd.array.dims.Time(data))

    assert array.data == data
    assert array.dims == ("time",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "time"


def test_chan() -> None:
    data = np.array([0], np.int64)
    array = asdataarray(sd.array.dims.Chan(data))

    assert array.data == data
    assert array.dims == ("chan",)
    assert array.dtype.type == data.dtype.type
    assert array.attrs[SHORT_NAME] == "chan"
