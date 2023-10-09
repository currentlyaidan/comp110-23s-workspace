"""Exercise 04 - Using Lists."""

__author__ = "730679404"

def all(nums: list[int], num: int) -> bool:
    """Returns True if all numbers match, returns False if they don't."""
    checker: int = 0
    # Check each number to see if they match.
    while (checker < len(nums)):
        if nums[checker] == num:
            checker += 1
        else:
            return False
    return True

def max(nums: list[int]) -> int:
    """Returns the largest value in a list of integers"""
    largest: int = 0
    checker: int = 0
    # Check if the list is empty, in which case print an error.
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    # Check each index on the list to figure out if the number is the largest.
    while (checker < len(nums)):
        if nums[checker] > largest:
            largest = nums[checker]
        checker += 1
    return largest

def is_equal(ints_one: list[int], ints_two: list[int]) -> bool:
    """Checks to see if each corresponding value in two lists are equal, returns False if not."""
    checker: int = 0
    # Make sure that the lists are of equal length first.
    if len(ints_one) != len(ints_two):
        return False
    # Check each value.
    while (checker < len(ints_one)):
        if ints_one[checker] == ints_two[checker]:
            checker += 1
        else:
            return False
    return True
