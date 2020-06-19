"""
This program calculates triangles area and displays the output in descending order of their area.
After adding each new triangle, the program asks if the user wants to add another one.
"""

import math
from operator import itemgetter


def create_triangle_data() -> list:
    """
    After user input in the format <name>, <side length>, <side length>, <side length> function creates
    a list with the data of each triangle.
    """
    triangle_data = []
    while True:
        sides_input = input("Input the triangle name and length of 3 sides of it using comma: ").split(', ')
        if len(sides_input) == 4:
            triangle_data.append([sides_input[0], sides_input[1], sides_input[2], sides_input[3]])

            response = input("Continue ? ").lower()
            if response != 'yes' and response != 'y':
                break
        else:
            print("Please, enter correct values!")
    return triangle_data


def get_triangle_area() -> dict:
    """The area of the triangle is calculated by the Heron formula."""
    global area, name
    triangle_data = create_triangle_data()
    result = {}
    for triangle in triangle_data:
        name = triangle[0]
        side1 = float(triangle[1])
        side2 = float(triangle[2])
        side3 = float(triangle[3])
        semiperimeter = float((side1 + side2 + side3) / 2)
        area = float(
            math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)))
        result[name] = round(area, 2)
    return result


def get_sorted_result() -> None:
    """In the created dictionary the data of the triangles are sorted in descending order of their area."""
    result = get_triangle_area()
    for key, value in sorted(result.items(), key=itemgetter(1), reverse=True):
        print(f'[Triangle {key}]: {value} cm')


if __name__ == '__main__':
    get_sorted_result()
