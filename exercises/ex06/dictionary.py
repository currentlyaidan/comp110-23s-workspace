"""EX06 Dictionary."""

__author__ = "730679404"


def invert(inverse: dict[str, str]) -> dict[str, str]:
    """Inverts the two values in a list."""
    inverted: dict[str, str] = {}
    for key in inverse:
        if inverse[key] in inverted:
            raise KeyError("KeyError")
        inverted[inverse[key]] = key
    return inverted


def favorite_color(pref: dict[str, str]) -> str:
    """Returns the most popular color."""
    popularity: dict[str, int] = {}
    popcolor: str = ""
    count: int = 0
    for key in pref:
        if pref[key] in popularity:
            popularity[pref[key]] += 1
        else:
            popularity[pref[key]] = 1
    for color in popularity:
        if popularity[color] > count:
            count = popularity[color]
            popcolor = color
    return popcolor


def count(words: list[str]) -> dict[str, int]:
    """Returns the amount of time a word is listed."""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(words):
        if words[idx] in result:
            result[words[idx]] += 1
        else:
            result[words[idx]] = 1
        idx += 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Return a list of values sorted by the first letter of the word."""
    result: dict[str, list[str]] = {}
    idx: int = 0
    lowercase: str = ""
    while idx < len(words):
        lowercase = words[idx]
        lowercase = lowercase.lower()
        if lowercase[0] in result:
            result[lowercase[0]].append(lowercase)
        else:
            result[lowercase[0]] = list()
            result[lowercase[0]].append(lowercase)
        idx += 1
    return result


def update_attendance(inputs: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Receive inputs and update the attendance log."""
    if day in inputs:
        inputs[day].append(student)
    else:
        inputs[day] = list()
        inputs[day].append(student)
    return inputs


def main() -> None:
    """The body of my program."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Eren", "Mikasa"], "Tuesday": ["Mikasa"]}
    print(update_attendance(attendance_log, "Tuesday", "Eren"))
    print(update_attendance(attendance_log, "Wednesday", "Armin"))


if __name__ == "__main__":
    main()