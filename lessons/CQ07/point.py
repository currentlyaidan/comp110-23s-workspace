"""CQ07."""

from __future__ import annotations


class Point:
    """Point on an x and y plane."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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