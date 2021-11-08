# dependencies
import sdarray as sd


# test functions
def test_author() -> None:
    assert sd.__author__ == "Akio Taniguchi"


def test_version() -> None:
    assert sd.__version__ == "0.1.3"
