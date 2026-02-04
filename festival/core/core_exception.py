"""The `exception` in all the `festival.core`."""

from festival.main_exception import FestivalBaseException

class InvalidHexColorFormatError(FestivalBaseException):
    """This exception is thrown if the HEX color format is invalid."""
    pass

class InvalidRGBColorFormatError(FestivalBaseException):
    """This exception is thrown if the RGB color format is invalid."""
    pass

class UnsupportedColorFormatError(FestivalBaseException):
    """This exception is thrown if the color format is unsupported."""
    pass