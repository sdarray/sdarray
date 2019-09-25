import sdarray as sd


def test_version():
    """Make sure the version is valid."""
    assert sd.__version__ == "0.0.1"


def test_author():
    """Make sure the author is valid."""
    assert sd.__author__ == "Akio Taniguchi"
