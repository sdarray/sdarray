# flake8: noqa
__version__ = "0.0.1"
__author__ = "Akio Taniguchi"


ACCESSOR = "sd"
DIMS = ("t", "ch")


from . import config
from . import arrayfact
from . import arrayfunc
from . import accessor
from .arrayfact import *
from .arrayfunc import *
