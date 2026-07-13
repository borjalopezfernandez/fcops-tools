"""FLEX FLORIS MODES"""

from typing import Any

_FLORIS_MODE_MAP = {
    0: "OBS___",
    1: "DARKNP",
    11: "DARKSR",
    20: "DEFRTS",
    21: "DEFDAR",
    25: "DARKOC",
    31: "DRKMTF",
    32: "DARKSTR",
    51: "SUN___",
    52: "DEFSUN",
    53: "MOON__",
    54: "CLOUD_",
    61: "MOONSL",
    71: "LINDES",
    72: "LINSEA",
    73: "LINSUN",
    74: "LINDAR",
    81: "CTE___",
}


def get_floris_mode_label(mode_code: Any) -> str:
    """Convert a FLORIS mode code to its 6-character mode label.

    Args:
        mode_code: Integer or string containing the FLORIS mode code.

    Returns:
        The mode label string.

    Raises:
        ValueError: If the mode code is not a valid integer or not recognized.
    """
    try:
        mode_code_int = int(mode_code)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"FLORIS mode code must be an integer-like value, got: {mode_code!r}") from exc

    if mode_code_int not in _FLORIS_MODE_MAP:
        raise ValueError(f"Unknown FLORIS mode code: {mode_code_int}")

    return _FLORIS_MODE_MAP[mode_code_int]
