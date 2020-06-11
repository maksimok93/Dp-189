"""
The program determines whether the envelope (with 'a' and 'b' side)
can be inserted into another envelope (with 'c' and 'd' side).
After each calculation, the program asks the user if he wants to continue.
"""


def check_correct_input():
    """Checking user input of positive numbers."""
    a = input("Enter the 1st side of 1st envelope: ")
    b = input("Enter the 2nd side of 1st envelope: ")
    c = input("Enter the 1st side of 2nd envelope: ")
    d = input("Enter the 2nd side of 2nd envelope: ")
    while True:
        try:
            a, b, c, d = float(a), float(b), float(c), float(d)
            if a <= 0:
                raise ValueError
            elif b <= 0:
                raise ValueError
            elif c <= 0:
                raise ValueError
            elif d <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please, enter a positive numbers! ")
            a = input("Enter the 1st side of 1st envelope: ")
            b = input("Enter the 2nd side of 1st envelope: ")
            c = input("Enter the 1st side of 2nd envelope: ")
            d = input("Enter the 2nd side of 2nd envelope: ")
    return a, b, c, d


def check_envelope_sides():
    """Comparing the lengths of the sides of envelopes for the possibility of inserting."""
    a, b, c, d = check_correct_input()
    if d > c:
        if (c <= a and c <= b) and (d <= a or d <= b):
            return "The 2nd envelope can be placed in the 1st."
        else:
            return "The 2nd envelope can't be placed in the 1st"

    elif c > d:
        if (d <= a and d <= b) and (c <= a or c <= b):
            return "The 2nd envelope can be placed in the 1st."
        else:
            return "The 2nd envelope can't be placed in the 1st"
    else:
        if (d <= a and d <= b) and (c <= a and c <= b):
            return "The 2nd envelope can be placed in the 1st."
        else:
            return "The 2nd envelope can't be placed in the 1st"


if __name__ == '__main__':
    while True:
        print(check_envelope_sides())
        response = input('Would you like to run the program again (Yes / No)? ').lower()
        if response != 'yes' and response != 'y':
            break
