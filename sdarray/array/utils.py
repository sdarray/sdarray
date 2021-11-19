# standard library
from typing import Any, Type, TypeVar


# type hints
T = TypeVar("T")


# utility classes
class KeywordOnly:
    """Limit the second and subsequent ``__init__`` args to be keyword-only."""

    def __new__(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        if len(args) > 1:
            raise TypeError("The second and subsequent args are keyword-only.")

        return super().__new__(cls)
