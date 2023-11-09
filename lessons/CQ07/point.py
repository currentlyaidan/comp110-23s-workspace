"""CQ07."""

from __future__ import annotations


class Point:
    """Point on an x and y plane."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Assign parameters."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale the point by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Create a new point a factor away from the old point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Prints the coordinates in a readable way."""
        readable: str = f"x: {self.x}; y: {self.y}"
        return readable
    
    def __mul__(self, factor: int | float) -> Point:
        """Creates a new point when you use the multiplication operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, increment: int | float) -> Point:
        """Creates a new point when you use the addition operator."""
        new_point: Point = Point(self.x + increment, self.y + increment)
        return new_point


my_Point: Point = Point()
new_Point: Point = my_Point + 3.5
print(str(my_Point))
print(new_Point)