"""Combining two lists into a dictionary."""

__author__ = "730679404"


def zip(first: list[str], second: list[int]) -> dict[str, int]:
    """Combine two lists into a dictionary."""
    zipped: dict[str, int] = {}
    idx: int = 0
    if len(first) != len(second):
        return zipped
    while idx < len(first):
        zipped[first[idx]] = second[idx]
        idx += 1
    return zipped