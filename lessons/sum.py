"""Summing the elements of a list using different loops."""

__author__ = "730679404"


def w_sum(vals: list[float]) -> float: 
    """Uses a while loop."""
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float: 
    """Uses a for/in loop."""
    sum: float = 0
    for value in vals: 
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float: 
    """Uses a for/in range loop."""
    sum: float = 0
    for value in range(0, len(vals)): 
        sum += vals[value]
    return sum