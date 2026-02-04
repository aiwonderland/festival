from ._color_codes import COLOR_CODES
from ._is_terminal_supported import _is_terminal_supported
from ._validate_style import _validate_style
from ._get_colored_string import _get_colored_string

def _style_text(
    text,
    fg_color = None,
    bg_color = None, 
    effects = None, 
    reset_after = True 
):
    text_str = str(text) if text is not None else ""

    if not _is_terminal_supported():
        return text_str
    
    style_parts = []
    
    if fg_color and _validate_style(fg_color):
        style_parts.append(COLOR_CODES[fg_color])  # type: ignore
    
    if bg_color and _validate_style(bg_color):
        style_parts.append(COLOR_CODES[bg_color]) # type: ignore
    
    if effects and isinstance(effects, list):
        for effect in effects:
            if _validate_style(effect):
                style_parts.append(COLOR_CODES[effect]) # type: ignore
    
    styled_text = "".join(style_parts) + text_str
    
    if reset_after:
        styled_text += COLOR_CODES["reset"] # type: ignore
    
    return str(styled_text)


# class ColorfulText:
#     """"""

#     def __init__(self, text, color = "#ffc0cb"):
#         self.text = text
#         self.color = color
    
#     def __len__(self):
#         return len(self.text)
    
#     def __repr__(self):
#         return 

#     def _get_color_string(self):
#         return _get_colored_string(self.text, self.color)
    


