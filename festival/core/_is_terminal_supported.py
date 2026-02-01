"""Auxiliary judgment: 
Determine whether the current terminal supports ANSI color escape codes.
If not supported, it will automatically downgrade to plain text output to avoid garbled characters."""

import sys

def _is_terminal_supported(): 
    is_tty = sys.stdout.isatty()
    is_windows = sys.platform.startswith("win")
    
    if is_tty or (is_windows and sys.version_info >= (3, 6)):
        return True
    return False