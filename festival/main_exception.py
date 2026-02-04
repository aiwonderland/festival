"""The `exception` in all the festival."""

class FestivalBaseException(Exception):
    """The base error exception in the `festival`."""
    def __init__(self, message):
        super().__init__(message)

class BarValueError(FestivalBaseException, ValueError):
    """If the `progress` of the `Bar` is less than or equal to 0, throw this error."""
    pass

