"""Testing all functions of the dictionary."""

__author__ ="730679404"

import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance

# test invert function

def test_one_item_dictionary() -> None:
    """invert({ one item dictionary }) will return the item inverted."""
    assert invert({"levi": "ackerman"}) == {'ackerman': 'levi'}


def test_two_item_dictionary_invert() -> None:
    """invert({ two item dictionary }) will return the two items in the dictionary inverted."""
    assert invert({"eren": "jaegar", "mikasa": "ackerman"}) == {'jaegar': 'eren', 'ackerman': 'mikasa'}


def test_no_item_dictionary_invert() -> None:
    """invert({ empty dictionary }) will return an empty dictionary in the edge case when there are no inputs in the dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}

# test favorite_color function

def test_short_favorite_color() -> None:
    """favorite_color({ short dictionary }) returns blue, the most popular color."""
    test_dict: dict[str, str] = {"reiner": "orange", "annie": "blue", "bertholdt": "blue", "eren": "red", "armin": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_long_favorite_color() -> None:
    """favorite_color({ long dictionary }) will return "teal", the most popular color."""
    test_dict: dict[str, str] = {"levi": "teal", "floch": "green", "hange": "teal", "erwin": "teal", "giles": "teal", "zeke": "green", "oluo": "yellow", "moblit": "teal", "theo": "teal", "petra": "pink"}
    assert favorite_color(test_dict) == "teal"


def test_no_favorite_color() -> None:
    """favorite_color({ empty dictionary }) will return no dictionary in the edge case when no items are in the dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""

# test count function

def test_three_two_one_list() -> None:
    """count() will return a dictionary, citing that each word has been said either one, two, or three times."""
    test_list: list[str] = ["scarf", "fight", "scarf", "scarf", "titan", "titan"]
    assert count(test_list) == {'scarf': 3, 'fight': 1, "titan": 2}


def test_fifteen_item_list() -> None:
    """count() will return a dictionary, listing the times each word has been said in a fifteen word list."""
    test_list: list[str] = ["scarf", "fight", "rage", "rage", "scarf", "battle", "warrior", "soldier", "fight", "scarf", "scarf", "blade", "warrior", "scarf", "finale"]
    assert count(test_list) == {'scarf': 5, 'fight': 2, 'rage': 2, 'battle': 1, 'warrior': 2, 'soldier': 1, 'blade': 1, 'finale': 1}


def test_empty_list() -> None:
    """count() will return an empty dictionary in the edge case of when there are no inputs in the list argument."""
    test_list: list[str] = []
    assert count(test_list) == {}

# test alphabetizer

def test_short_list() -> None:
    """alphabetizer() will return each item sorted by the first letter of the word."""
    test_list: list[str] = ["happiness", "became", "bright", "the", "hearts", "battle", "gave"]
    assert alphabetizer(test_list) == {'h': ['happiness', 'hearts'], 'b': ['became', 'bright', 'battle'], 't': ['the'], 'g': ['gave']}


def test_speech_alphabetized() -> None:
    """alphabetizer() will sort the words from a speech by the letter that each word begins with."""
    test_list: list[str] = ['are', 'you', 'watching', 'us', 'waiting', 'to', 'see', 'what', 'became', 'of', 'the', 'hearts', 'you', 'gave']
    assert alphabetizer(test_list) == {'a': ['are'], 'y': ['you', 'you'], 'w': ['watching', 'waiting', 'what'], 'u': ['us'], 't': ['to', 'the'], 's': ['see'], 'b': ['became'], 'o': ['of'], 'h': ['hearts'], 'g': ['gave']}


def test_cloned_word() -> None:
    """alphabitizer() will return a list of all of the same word in the edge case when all of the words in the list are identical."""
    test_list: list[str] = ["go", "go", "go", "go", "go", "go", "go", "go", "go", "go"]
    assert alphabetizer(test_list) == {'g': ['go', 'go', 'go', 'go', 'go', 'go', 'go', 'go', 'go', 'go']}

# test update_attendance

def test_one_on_monday() -> None:
    """update_attendance will add a student who was present on monday."""
    before: dict[str, list[str]] = {"Monday": ["Megumi", "Nobara"], "Tuesday": ["Itadori", "Megumi"], "Wednesday": ["Megumi"]}
    assert update_attendance(before, "Monday", "Itadori") == {'Monday': ['Megumi', 'Nobara', 'Itadori'], 'Tuesday': ['Itadori', 'Megumi'], 'Wednesday': ['Megumi']}


def test_new_day() -> None:
    """update_attendance will add a student on a new day."""
    before: dict[str, list[str]] = {"Monday": ["Megumi", "Nobara"], "Tuesday": ["Megumi"], "Wednesday": ["Itadori"]}
    assert update_attendance(before, "Thursday", "Nobara") == {'Monday': ['Megumi', 'Nobara'], 'Tuesday': ['Megumi'], 'Wednesday': ['Itadori'], 'Thursday': ['Nobara']}


def test_empty_log() -> None:
    """update_attendance will add to a log in the edge case when the existing attendance log is empty."""
    before: dict[str, list[str]] = {}
    assert update_attendance(before, "Monday", "Megumi") == {'Monday': ['Megumi']}