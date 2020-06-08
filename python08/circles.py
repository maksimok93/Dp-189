"""
This program for a given circle radius calculates its diameter, area and perimeter.
The program accepts for input: < circle identifier >, < radius >, < circle color >.
At the request of the user, the program can change the color of the circle to a new one.
"""
import math
from typing import Dict


def safe_radius_of(number: float) -> float:
    """Check whether the entered number is an int or float number."""
    if not (
            isinstance(number, int) or
            isinstance(number, float)
    ):
        raise TypeError('Radius should be either "int" or "float" data type!')
    if number < 0:
        raise ValueError('Radius value should be more that "0"!')
    return number


def calculate_square_of(number: float) -> float:
    """Get the square of the entered number."""
    return number ** 2


def multiply_by_pi(number: float) -> float:
    """Get the multiply of pi_number and the entered number."""
    return math.pi * number


def double_of(number: float) -> float:
    """Get a double of the entered number."""
    return number * 2


class Circle:
    """
    Single circle is characterized by three values.
    They're identifier of each circle, circle radius and circle color.
    """

    def __init__(self, identifier: int, radius: float, color: str) -> None:
        """Create an instance of the Circle class according to the three entered parameters."""
        self.identifier = identifier
        self._radius = lambda: safe_radius_of(radius)
        self._color = color

    def change_color(self, color: str) -> None:
        """Check whether the entered circle color has the 'str' data type."""
        if not isinstance(color, str):
            raise TypeError('Color should be "str" data type!')
        self._color = color

    def diameter(self) -> float:
        """Get the diameter for the circle instance."""
        return double_of(self._radius())

    def area(self) -> float:
        """Get the area for the circle instance."""
        return multiply_by_pi(calculate_square_of(self._radius()))

    def perimeter(self) -> float:
        """Get the perimeter for the circle instance."""
        return double_of(multiply_by_pi(self._radius()))

    def __str__(self) -> str:
        """Display information about calculated circle instance radius and entered color."""
        return f'Circle(radius = {self._radius()}, color = "{self._color}")'


class Circles:
    """Circles class consists of Circle class instances. Using it we collect data for each circle into one instance."""

    def __init__(self, *circles: Circle) -> None:
        """Combine all instances of Circle class into one."""
        self._circles = circles

    def update_colors(self, new_colors: Dict[int, str]) -> None:
        """Update circle color for each circle instance if the user enters a new color."""
        for identifier, color in new_colors.items():
            this = self.find(identifier)
            this.change_color(color)

    def find(self, identifier: int) -> Circle:
        """
        Find circle instance according its identifier.
        If the user enters a non-existent identifier -  exception will be raised.
        """
        for this in self._circles:
            if this.identifier == identifier:
                return this

        raise ValueError(f"There is no circle with this identifier: {identifier}")

    def show_diameters(self) -> None:
        """Get output of the diameter of each circle instance."""
        for circle in self._circles:
            print(f"A diameter of {circle} is {circle.diameter()}")

    def show_areas(self) -> None:
        """Get output of an area of each circle instance."""
        for circle in self._circles:
            print(f"An area of {circle} is {round(circle.area(), 2)}")

    def show_perimeters(self) -> None:
        """Get output of the perimeter of each circle instance."""
        for circle in self._circles:
            print(f"A perimeter of {circle} is {round(circle.perimeter(), 2)}")


if __name__ == "__main__":
    circles = Circles(
        Circle(1, 1, 'red'),
        Circle(2, 0.2, 'super-red'),
        Circle(3, 3, 'green'),
        Circle(4, 5, 'super-green'),
    )
    circles.show_diameters()
    circles.show_areas()
    circles.show_perimeters()
    circles.update_colors({1: 'blue', 2: 'red', 3: 'black', 4: 'purple'})

    circles.show_perimeters()
