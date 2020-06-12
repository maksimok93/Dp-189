"""
This program calculates triangles area and displays the output in descending order of their area.
After adding each new triangle, the program asks if the user wants to add another one.
"""

import math


class Triangle:
    result = {}

    def __init__(self, name, side1, side2, side3) -> None:
        """
        After user input in the format <name>, <side length>, <side length>, <side length>,
        class constructor creates an instance of a triangle.
        """
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_triangle_area(self) -> float:
        """Finding the area of a triangle using Heron's formula."""
        semiperimeter = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(
            semiperimeter * (semiperimeter - self.side1) * (semiperimeter - self.side2) * (semiperimeter - self.side3))
        return round(area, 2)

    @classmethod
    def get_sort_triangles(cls) -> None:
        """In the created dictionary the data of the triangles are sorted in descending order of their area."""
        sorted_triangles = sorted(cls.result.items(), key=lambda x: x[1], reverse=True)
        for triangle in sorted_triangles:
            print(f'[Triangle {triangle[0]}]: {triangle[1]} cm')


if __name__ == '__main__':
    triangle_data = []
    while True:
        sides = input("Input the triangle name and length of 3 sides of it using comma: ").split(', ')
        if len(sides) == 4:
            triangle_data.append([sides[0], sides[1], sides[2], sides[3]])
            response = input("Do you want to add another triangle? ").lower()
            if response != 'yes' and response != 'y':
                break
        else:
            print("Expected for user input 4 arguments, " "got %d instead!" % len(sides))

    for triangle in triangle_data:
        name = triangle[0]
        side1 = float(triangle[1])
        side2 = float(triangle[2])
        side3 = float(triangle[3])
        triangle = Triangle(name, side1, side2, side3)
        Triangle.result[triangle.name] = triangle.get_triangle_area()

    Triangle.get_sort_triangles()
