"""Test my zip function."""

__author__ = 730679404

from lessons.zip import zip


def test_empty_lists() -> None:
    """Test when given empty lists."""
    test_list_int: list[int] = []
    test_list_str: list[str] = []
    assert zip(test_list_int, test_list_str) == {}


def test_two_item_lists() -> None:
    """Test when given lists with two items."""
    test_list_int: list[int] = [1, 2]
    test_list_str: list[str] = ["hi", "wsg gang"]
    assert zip(test_list_int, test_list_str) == {1: 'hi', 2: 'wsg gang'}


def test_one_item_lists() -> None:
    """Test when given lists with one item."""
    test_list_int: list[int] = [1]
    test_list_str: list[str] = ["valorant"]
    assert zip(test_list_int, test_list_str) == {1, 'valorant'}