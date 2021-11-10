# dependencies
import numpy as np
import sdarray as sd
from xarray_dataclasses import asdataarray


# test functions
def test_time() -> None:
    data = np.array(["2000-01-01"], np.datetime64)
    time = asdataarray(sd.dims.Time(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype.type == data.dtype.type


def test_chan() -> None:
    data = np.array([0], np.int64)
    chan = asdataarray(sd.dims.Chan(data))

    assert chan.data == data
    assert chan.dims == ("chan",)
    assert chan.dtype.type == data.dtype.type
