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

print(max([]))