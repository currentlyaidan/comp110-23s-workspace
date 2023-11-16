"""File to define Fish class."""


class Fish:
    """Creates a fish."""
    age: int

    def __init__(self, age: int = 0):
        """Defines a fishy."""
        self.age = age
        return None
    
    def one_day(self):
        """What happens to the fish in a day."""
        self.age += 1
        return None