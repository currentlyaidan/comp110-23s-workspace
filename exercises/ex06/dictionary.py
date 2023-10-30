"""EX06 Dictionary"""

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
    popularity: dict[str,int] = {}
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
    for word in words:
        if words[word] in result:
            result[words[word]] += 1
        else:
            result[words[word]] = 1
    return result


def main() -> None:
    """The body of my program."""
    print(count[ "hi", "hi", "smart", "hi", "sup", "hi"])

if __name__ == "__main__":
    main()