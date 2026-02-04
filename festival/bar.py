from functools import total_ordering
from .core._bar import _Bar

__all__ = [
    "Bar"
]
@total_ordering
class Bar(_Bar):
    """Single-line progress bar.

    :param current: Current progress (completed count, must be >= 0)
    :param total: Total progress (total count, must be > 0)
    :param prefix: Prefix text of the progress bar (default "Progress")
    :param width: Width of the progress bar (number of characters, default 30)
    :param fill_char: Filling character for the completed part (default "#")
    :param empty_char: Filling character for the incomplete part (default "-")"""

    def __init__(self, current=30, total=100, prefix="Progress", width=30, fill_char="#", empty_char="-"):
        super().__init__(current, total, prefix, width, fill_char, empty_char)

    def draw(self):
        return super()._draw()
    
    def __repr__(self):
        return super().__repr__()
    
    def __hash__(self):
        return super().__hash__()
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    def __gt__(self, other):
        return super().__gt__(other)
