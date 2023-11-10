"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        for fanimal in self.fish:
            if fanimal.age < 3:
                surviving_fish.append(fanimal)
        for banimal in self.bears:
            if banimal.age < 5:
                surviving_bears.append(banimal)    
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        fish_list: list[Fish] = self.fish
        while idx < amount:
            fish_list.pop(0)
            idx += 1
        self.fish = fish_list
        return None

    def bears_eating(self):
        for banimal in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                banimal.eat(3)
        return None
    
    def check_hunger(self):
        survivors: list[Bear] = self.bears
        idx: int = 0
        while idx < len(self.bears):
            if self.bears[idx].hunger_score == 0:
                survivors.pop(idx)
            idx += 1
        self.bear = survivors
        return None
        
    def repopulate_fish(self):
        offspring: int = 0
        if len(self.fish) >=  2:
            offspring = (len(self.fish) // 2) * 4
            while offspring > 0:
                self.fish.append(Fish())
                offspring -= 1
        return None
    
    def repopulate_bears(self):
        offspring: int = 0
        if len(self.bears) >= 2:
            offspring = (len(self.bears) // 2)
            while offspring > 0:
                self.bears.append(Bear())
                offspring -= 1
        return None
    
    def view_river(self):
        status: str = f"~~~ Day {self.day}: ~~~ \n"
        status += f"Fish population: {len(self.fish)} \n"
        status += f"Bear population: {len(self.bears)}"
        print(status)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates a week."""
        times: int = 0
        while times < 7:
            self.one_river_day()
            times += 1