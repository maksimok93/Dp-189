def figure_size_input():
    """To create a figure we need to input its dimensions."""
    a = input("Enter the height of the picture: ")
    b = input("Enter the width of the picture: ")

    while True:
        try:
            a = int(a)
            b = int(b)
            break
        except:
            print("Please, input the correct values! ")
            a = input("Enter the height of the picture: ")
            b = input("Enter the width of the picture: ")
    return a, b


def get_board():
    """This function iterates entered dimensions using space and symbol '*' as strings."""
    symbol = '*'
    space = ' '
    a, b = figure_size_input()
    for item in range(1, a + 1):
        if (item + 2) % 2 == 0:
            print(b * (space + symbol))
        else:
            print(b * (symbol + space))


if __name__ == '__main__':
    get_board()
