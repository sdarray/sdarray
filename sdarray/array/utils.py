# standard library
from typing import Any, Type, TypeVar


# dependencies
from astropy.units import Quantity


# type hints
T = TypeVar("T")


# utility classes
class KeywordOnly:
    """Limit the second and subsequent ``__init__`` args to be keyword-only."""

    def __new__(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        if len(args) > 1:
            raise TypeError("The second and subsequent args are keyword-only.")

        return super().__new__(cls)


class UnitConversion:
    """Convert data to the defined units if they are given with units."""

    def __post_init__(self) -> None:
        if not (hasattr(self, "data") and hasattr(self, "units")):
            return

        if isinstance(self.data, Quantity):
            self.data = self.data.to(self.units).value  # type: ignore
