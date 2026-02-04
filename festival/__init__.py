"""This library can enhance the fun and enjoyment of terminal output, 
adding features such as differently colored fonts and progress bars."""

import festival.version as v

from .core import COLOR_CODES
from .text import style_text
from .bar import Bar
import festival.exceptions as exceptions

__version__ = v.__version__
__author__ = v.__author__
__copyright__ = v.__copyright__
__email__ = v.__email__
__description__ = v.__description__
__date__ = v.__date__
__contact__ = v.__contact__
__all_author__ = v.__all_author__
__license__ = v.__license__ 
__url__ = v.__url__
__download_url__ = v.__download_url__

__all__ = [
    "COLOR_CODES",
    "style_text",
    "Bar",
    "exceptions"
]