"""EX06 Dictionary"""

def invert(inverse: dict[str, str]) -> dict[str, str]:
    """Inverts the two values in a list."""
    idx: int = 0
    inverted: dict[str, str] = {}
    for key in inverse:
        if inverse[key] in inverted:
            raise KeyError("KeyError")
        inverted[inverse[idx]] = key
        idx += 1
    return inverted


def favorite_color(pref: dict[str, str]) -> str:
    """Returns the most popular color."""
    invert(pref)
    idx: int = 0
    if pref[idx] in pref: