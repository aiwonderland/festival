from .core import _style_text, _print_password

__all__ = [
    "style_text",
    "print_password"
]
def style_text(
    text,
    fg_color = None,
    bg_color = None, 
    effects = None, 
    reset_after = True 
):
    """
    Enhanced custom text styling: supports foreground color, background color, and combined multiple text effects.

    :param text: The text content to be formatted
    :param fg_color: Foreground color (optional, refer to the foreground color entries in COLOR_CODES, e.g., "red", "black_fg")
    :param bg_color: Background color (optional, refer to the background color entries in COLOR_CODES, e.g., "green_bg", "blue_bg_bright")
    :param effects: List of text effects (optional, e.g., ["bold", "underline"], refer to the basic control entries in COLOR_CODES)
    :param reset_after: Whether to reset all styles at the end of the text (default True)
    :return: Formatted text (returns the original text if not supported by the terminal)
    """
    return _style_text(text=text,
                fg_color=fg_color,
                bg_color=bg_color,
                effects=effects,
                reset_after=reset_after)
    
def print_password(prompt = "Enter password: "):
    """
    Password input prompt (input content hidden, demonstrating the `hidden` effect only)

    :param porompt: Text displayed before prompting for password input.
    :return: The password entered by the user
    """
    return _print_password(prompt=prompt)
    