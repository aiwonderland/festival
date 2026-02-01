from ._color_codes import COLOR_CODES
from ._is_terminal_supported import _is_terminal_supported
from ._validate_style import _validate_style

def _style_text(
    text,
    fg_color = None,
    bg_color = None, 
    effects = None, 
    reset_after = True 
):
    if not _is_terminal_supported():
        return str(text)
    
    style_parts = []
    
    if fg_color and _validate_style(fg_color):
        style_parts.append(COLOR_CODES[fg_color])
    
    if bg_color and _validate_style(bg_color):
        style_parts.append(COLOR_CODES[bg_color])
    
    if effects and isinstance(effects, list):
        for effect in effects:
            if _validate_style(effect):
                style_parts.append(COLOR_CODES[effect])
    
    styled_text = "".join(style_parts) + str(text)
    
    if reset_after:
        styled_text += COLOR_CODES["reset"]
    
    return styled_text

def _print_password(prompt = "Enter password: "):
    print(_style_text(prompt, fg_color="blue", effects=["bold"]), end="")
    password = input(_style_text("", effects=["hidden"]))
    print(COLOR_CODES["reset"])
    return password
