"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Creates a bear."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """What happens to the bear in a day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """A bear's gotta eat."""
        self.hunger_score += num_fish
        return None