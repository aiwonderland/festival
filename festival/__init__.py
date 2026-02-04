"""This library can enhance the fun and enjoyment of terminal output, 
adding features such as differently colored fonts and progress bars."""

from __version__ import (
    __author__,
    __all_author__,
    __contact__,
    __copyright__,
    __date__,
    __description__,
    __download_url__,
    __email__,
    __license__,
    __url__,
    __version__
)

from .core import COLOR_CODES
from .text import style_text
from .bar import Bar
import festival.exceptions as exceptions

__all__ = [
    "COLOR_CODES",
    "style_text",
    "Bar",
    "exceptions"
]