# flake8: noqa
__version__ = "0.1.2"
__author__ = "Akio Taniguchi"


ACCESSOR = "sd"
DIMS = ("t", "ch")


from . import specs
from . import config
from . import arrayfact
from . import arrayfunc
from . import selector
from . import accessor
from .arrayfact import *
from .arrayfunc import *


# for sphinx apidoc
__all__ = dir()
