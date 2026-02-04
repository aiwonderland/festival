from .core_exception import InvalidHexColorFormatError, InvalidRGBColorFormatError, UnsupportedColorFormatError

def _get_colored_string(content, color):
    ANSI_COLOR_PREFIX = "\033[38;2;"  
    ANSI_RESET = "\033[0m"            

    r, g, b = None, None, None

    if isinstance(color, str):
        clean_hex = color.strip().lstrip("#").lower()

        if len(clean_hex) != 6 or not clean_hex.isalnum():
            raise InvalidHexColorFormatError("Invalid hex color format. Correct format examples: #ffc0cb or ffc0cb")

        try:
            r = int(clean_hex[0:2], 16)
            g = int(clean_hex[2:4], 16)
            b = int(clean_hex[4:6], 16)
        except ValueError:
            raise InvalidHexColorFormatError("Hex color contains invalid characters. Only 0-9, a-f, A-F are supported.")

    elif isinstance(color, (tuple, list)) and len(color) == 3:
        r, g, b = color

        for channel in [r, g, b]:
            if not isinstance(channel, int) or not (0 <= channel <= 255):
                raise InvalidRGBColorFormatError("Invalid RGB color value. r/g/b must be integers between 0 and 255.")

    else:
        raise UnsupportedColorFormatError("Unsupported color format. Only hex strings (e.g., #ffc0cb) or RGB tuples (e.g., (255,192,203)) are supported.")

    colored_str = f"{ANSI_COLOR_PREFIX}{r};{g};{b}m{content}{ANSI_RESET}"
    return colored_str