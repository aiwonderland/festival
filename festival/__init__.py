"""This library can enhance the fun and enjoyment of terminal output, 
adding features such as differently colored fonts and progress bars."""

from .text import style_text, print_password

__version__ = "0.0.0"

__all__ = [
    "style_text",
    "print_password"
]