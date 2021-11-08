# dependencies
import numpy as np
import sdarray as sd
from xarray_dataclasses import asdataarray


# test functions
def test_time() -> None:
    data = np.array(["2000-01-01"], "M8[ns]")
    time = asdataarray(sd.dims.Time(data))

    assert time.data == data
    assert time.dims == ("time",)
    assert time.dtype == data.dtype


def test_chan() -> None:
    data = np.array([0], "i8")
    chan = asdataarray(sd.dims.Chan(data))

    assert chan.data == data
    assert chan.dims == ("chan",)
    assert chan.dtype == data.dtype
