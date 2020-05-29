"""Array creator module.

"""
__all__ = ["ArrayDef", "CoordDef", "array_creator"]


# standard library
from dataclasses import dataclass
from datetime import datetime
from textwrap import dedent, indent, wrap
from typing import Callable, Hashable, Sequence, Union


# dependent packages
import numpy as np
from xarray import DataArray


# constants
INDENT = " " * 4
ELEMENT_TYPES = bool, str, int, float, datetime


# type aliases
Array = Union[np.ndarray, Union[ELEMENT_TYPES]]
Dtype = Union[np.dtype, type, str]
Dims = Union[Hashable, Sequence[Hashable]]
Element = Union[ELEMENT_TYPES]
Shape = Sequence[int]


# data classes
@dataclass(frozen=True)
class ArrayDef:
    """Definition of array."""

    name: str  #: Name of array.
    dims: Dims  #: Dimensions of array.
    short_desc: str  #: Short description.
    long_desc: str = ""  #: Long description (if any).

    @property
    def docstring(self) -> str:
        """String for function's docstring."""
        return (
            f"{self.name}: "
            f"{self.short_desc} "
            f"{self.long_desc} "
            f"Dims: ``{self.dims}``."
        )

    @property
    def docstring_wrapped(self) -> str:
        """String for function's docstring (wrapped)."""
        return f"\n{INDENT}".join(wrap(self.docstring))


@dataclass(frozen=True)
class CoordDef:
    """Definition of coordinate."""

    name: str  #: Name of coordinate.
    dims: Dims  #: Dimension(s) of coordinate.
    type: str  #: Type of value(s).
    default: Element  #: Default value(s).
    short_desc: str  #: Short description.
    long_desc: str = ""  #: Long description (if any).

    @property
    def docstring(self) -> str:
        """String for function's docstring."""
        return (
            f"{self.name}: "
            f"{self.short_desc} "
            f"{self.long_desc} "
            f"Dims: ``{self.dims}``. "
            f"Type: ``{self.type}``. "
            f"Default: ``{self.default!r}``."
        )

    @property
    def docstring_wrapped(self) -> str:
        """String for function's docstring (wrapped)."""
        return f"\n{INDENT}".join(wrap(self.docstring))


# main functions
def array_creator(cls: type) -> type:
    """Decorator which adds array creator functions (static methods) to class.

    Args:
        cls: Class which has class attributes (``array_def``, ``coord_defs``).

    Returns:
        cls: Class with creator functions (``array``, ``ones``, ``zeros``).

    Raises:
        AttributeError: Raised if class does not have
            either ``array_def`` or ``coord_defs``.

    """
    if not hasattr(cls, "array_def"):
        raise AttributeError("Class must have array_def attribute.")

    if not hasattr(cls, "coord_defs"):
        raise AttributeError("Class must have coord_defs attribute.")

    creator = get_creator(cls.array_def, cls.coord_defs)

    cls.__call__ = staticmethod(creator)
    cls.ones = staticmethod(get_ones(creator))
    cls.zeros = staticmethod(get_zeros(creator))

    return cls


# helper functions
def get_creator(array_def: ArrayDef, coord_defs: Sequence[CoordDef]) -> Callable:
    """Return creator function with given definitions of array and coordinates.

    Args:
        array_def: Definition of array.
        coord_defs: Sequence of coordinate definitions.

    Returns:
        creator: Creator function.

    """

    def creator(array: Array, **coords: Array) -> DataArray:
        """\
        Create DataArray from given array and coordinates.

        Args:
        {array}
        {coords}

        Returns:
            array: DataArray with given coordinates.

        """
        array = DataArray(array, dims=array_def.dims)

        for cd in coord_defs:
            coord = coords.get(cd.name, None)
            shape = [array.sizes[dim] for dim in cd.dims]

            if coord is None:
                coord = np.full(shape, cd.default)
            elif isinstance(coord, ELEMENT_TYPES):
                coord = np.full(shape, coord)

            array.coords[cd.name] = cd.dims, np.asarray(coord, cd.type)

        return array

    # update docstring
    doc_array = indent(array_def.docstring_wrapped, INDENT)
    doc_coords = indent("\n".join(cd.docstring_wrapped for cd in coord_defs), INDENT)
    creator.__doc__ = dedent(creator.__doc__).format(array=doc_array, coords=doc_coords)

    return creator


def get_ones(creator: Callable) -> Callable:
    """Return ones function based on given creator function."""

    def ones(shape: Shape, dtype: Dtype = float, **coords: Array) -> DataArray:
        """Create DataArray filled with ones from given shape and coordinates.

        Args:
            shape: Shape of array.
            dtype: Data type of array. Default: ``float64``.
            coords: Coordinates. See creator function for more details.

        Returns:
            array: DataArray filled with ones with given coordinates.

        """
        return creator(np.ones(shape, dtype), **coords)

    return ones


def get_zeros(creator: Callable) -> Callable:
    """Return zeros function based on given creator function."""

    def zeros(shape: Shape, dtype: Dtype = float, **coords: Array) -> DataArray:
        """Create DataArray filled with zeros from given shape and coordinates.

        Args:
            shape: Shape of array.
            dtype: Data type of array. Default: ``float64``.
            coords: Coordinates. See creator function for more details.

        Returns:
            array: DataArray filled with zeros with given coordinates.

        """
        return creator(np.zeros(shape, dtype), **coords)

    return zeros


def get_empty(creator: Callable) -> Callable:
    """Return empty function based on given creator function."""

    def empty(shape: Shape, dtype: Dtype = float, **coords: Array) -> DataArray:
        """Create uninitialized DataArray from given shape and coordinates.

        Args:
            shape: Shape of array.
            dtype: Data type of array. Default: ``float64``.
            coords: Coordinates. See creator function for more details.

        Returns:
            array: Uninitialized DataArray with given coordinates.

        """
        return creator(np.empty(shape, dtype), **coords)

    return empty


def get_full(creator: Callable) -> Callable:
    """Return full function based on given creator function."""

    def full(shape: Shape, fill_value: Element, **coords: Array,) -> DataArray:
        """Create uninitialized DataArray from given shape and coordinates.

        Args:
            shape: Shape of array.
            dtype: Data type of array. Default: ``float64``.
            coords: Coordinates. See creator function for more details.

        Returns:
            array: Uninitialized DataArray with given coordinates.

        """
        return creator(np.full(shape, fill_value), **coords)

    return full
