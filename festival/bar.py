from .core import _Bar

__all__ = [
    "Bar"
]
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
