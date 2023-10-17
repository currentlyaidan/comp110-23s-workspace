"""Summing the elements of a list using different loops."""

__author__ = "730679404"

vals: list[float] = [1.1, 0.9, 1.0]

def w_sum(nums = list[float]) -> float:
    """Uses a while loop."""
    idx: int = 0
    sum: float = 0
    while idx<len(list):
        sum += list[idx]
        idx += 1
    return sum

def f_sum(nums = list[float]) -> float:
    """Uses a for/in loop."""
    sum: float = 0
    for value in nums:
        sum += value
    return sum

def f_range_sum(nums = list[float]) -> float:
    """Uses a for/in range loop."""
    sum: float = 0
    for value in range(0,len(vals)):
        sum += value
    return sum