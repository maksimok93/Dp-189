def checking_correct_input():
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
    a, b, c, d = checking_correct_input()
    if d > c:
        if (c <= a and c <= b) and (d <= a or d <= b):
            print("The 2nd envelope can be placed in the 1st.")
        else:
            print("The 2nd envelope can't be placed in the 1st")

    elif c > d:
        if (d <= a and d <= b) and (c <= a or c <= b):
            print("The 2nd envelope can be placed in the 1st.")
        else:
            print("The 2nd envelope can't be placed in the 1st")
    else:
        if (d <= a and d <= b) and (c <= a and c <= b):
            print('OK')
        else:
            print('not OK')


def main():
    while True:
        check_envelope_sides()
        response = input('Would you like to run the program again (Yes / No)? ').lower()
        if response != 'yes' and response != 'y':
            break


if __name__ == '__main__':
    main()
