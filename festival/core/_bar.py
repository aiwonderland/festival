import sys
from functools import total_ordering

from festival.main_exception import BarValueError

@total_ordering
class _Bar:
    """Single-line progress bar."""

    def __init__(self, 
                 current = 30, 
                 total = 100,
                 prefix = "Progress",
                 width = 30,
                 fill_char = "#",
                 empty_char = "-"):
        if total <= 0:
            raise BarValueError("total must be greater than 0")
        if current < 0 or current > total:
            raise BarValueError("current must be between 0 and total")
        self.current = current
        self.total = total
        self.prefix = prefix
        self.width = width
        self.fill_char = fill_char
        self.empty_char = empty_char

    def __repr__(self):
        return (
            f"Bar(current={self.current}, "
            f"total={self.total}, "
            f"prefix={self.prefix!r}, "
            f"width={self.width}, "
            f"fill_char={self.fill_char!r}, "
            f"empty_char={self.empty_char!r})"
        )
    
    def __hash__(self):
        return hash((self.current, self.total, self.prefix, self.width, self.fill_char, self.empty_char))
    
    def __eq__(self, value):
        if not isinstance(value, _Bar):
            return False

        return (
            self.current == value.current
            and self.total == value.total
            and self.prefix == value.prefix
            and self.width == value.width
            and self.fill_char == value.fill_char
            and self.empty_char == value.empty_char
        )
    
    def __gt__(self, other):
        if not isinstance(other, _Bar):
            return False
        self_ratio = self.current / self.total
        other_ratio = other.current / other.total
        return self_ratio > other_ratio
    
    def _draw(self):
        """Draw the bar."""
        if self.current < 0:
            self.current = 0
        if self.current > self.total:
            self.current = self.total
        if self.width <= 0:
            self.width = 30

        percent = (self.current / self.total) * 100
        filled_length = int(self.width * (self.current / self.total))

        bar = self.fill_char * filled_length + self.empty_char * (self.width - filled_length)
        progress_text = f"\r{self.prefix}: [{bar}] {percent:.1f}%"

        sys.stdout.write(progress_text)
        sys.stdout.flush()

        if self.current == self.total:
            print()

