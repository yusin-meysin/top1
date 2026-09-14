# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: CourseSchedule
import sys

def colorize(text: str, fg: int = None, bg: int = None, bold: bool = False, dim: bool = False) -> str:
    """Apply ANSI color codes to a string.

    Args:
        text: The string to colorize.
        fg: Foreground color (1-15), None for default.
        bg: Background color (1-15), None for default.
        bold: Whether to make text bold.
        dim: Whether to make text dim.

    Returns:
        The colorized string, or the original if no color is specified.
    """
    if not (fg or bg or bold or dim):
        return text

    codes = []
    if bold:
        codes.append("1")
    if dim:
        codes.append("2")
    if fg is not None:
        codes.append(f"3{fg}" if fg < 10 else f"9{fg}")
    if bg is not None:
        codes.append(f"4{bg}" if bg < 10 else f"10{bg}")

    if not codes:
        return text

    prefix = f"\033[{','.join(codes)}m"
    suffix = "\033[0m"
    return f"{prefix}{text}{suffix}"


def colored_print(*args, fg=None, bg=None, bold=False, dim=False, **kwargs):
    """Print a colorized string.

    Args:
        *args: The strings to print.
        fg: Foreground color.
        bg: Background color.
        bold: Whether to make text bold.
        dim: Whether to make text dim.
        **kwargs: Additional keyword arguments.
    """
    text = " ".join(str(arg) for arg in args)
    print(colorize(text, fg=fg, bg=bg, bold=bold, dim=dim), **kwargs)


def disable_colors():
    """Disable colors by writing raw strings instead of colorized ones.

    Args:
        None.

    Returns:
        None.
    """
    sys.stdout = open(sys.stdout.fileno(), 'w', buffering=1)


def enable_colors():
    """Re-enable colors by restoring the original stdout.

    Args:
        None.

    Returns:
        None.
    """
    sys.stdout = open(sys.stdout.fileno(), 'wb', buffering=0)
