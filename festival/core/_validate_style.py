"""Auxiliary judgment: Verify whether the incoming style name is valid in `COLOR_CODES`."""

from ._color_codes import COLOR_CODES

def _validate_style(style_name):
    return style_name in COLOR_CODES