__all__ = ["array", "zeros", "ones"]

from functools import wraps
import numpy as np
import xarray as xr
import sdarray as sd


class use_coords:
    """Decorator that adds coordinates to a dataarray."""

    def __init__(self, config):
        self.config = dict(config)

    def __call__(self, func):
        @wraps(func)
        def wrapped(data, **kwargs):
            coord_kwargs = self.split_coord_kwargs(kwargs)
            array = func(data, **kwargs)
            self.add_coords(array, **coord_kwargs)
            return array

        return wrapped

    def split_coord_kwargs(self, kwargs):
        return {name: kwargs.pop(name, None) for name in self.config}

    def add_coords(self, array, **coord_kwargs):
        for name, info in self.config.items():
            coord = self.get_coord(array, coord_kwargs[name], **info)
            array.coords[name] = coord

    @staticmethod
    def get_coord(array, data=None, dims=None, dtype=int, default=0, **ignored):
        """Get an xarray's coordinate compatible with a dataarray."""
        if dims is None:
            dims = ()

        if isinstance(dims, str):
            dims = (dims,)

        if not set(dims) <= set(sd.DIMS):
            raise ValueError(f"dims must be a subset of {sd.DIMS}.")

        if data is None:
            shape = tuple(array.sizes[dim] for dim in dims)
            data = np.full(shape, default)

        data = np.asarray(data).astype(dtype)
        return xr.DataArray(data, dims=dims)


@use_coords(sd.config.coords)
def array(data, **kwargs):
    """Make a dataarray from data."""
    return xr.DataArray(data, dims=sd.DIMS, **kwargs)


def zeros(shape, dtype=None, **kwargs):
    """Make a dataarray filled with zeros."""
    return array(np.zeros(shape, dtype), **kwargs)


def ones(shape, dtype=None, **kwargs):
    """Make a dataarray filled with ones."""
    return array(np.ones(shape, dtype), **kwargs)