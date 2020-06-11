def figure_size_input():
    """To create a figure we need to input its dimensions."""
    height = input("Enter the height of the picture: ")
    width = input("Enter the width of the picture: ")

    while True:
        try:
            height = int(height)
            width = int(width)
            break
        except:
            print("Please, input the correct values! ")
            height = input("Enter the height of the picture: ")
            width = input("Enter the width of the picture: ")
    return height, width


def get_board():
    """This function iterates entered dimensions using space and symbol '*' as strings."""
    height, width = figure_size_input()
    for item in range(1, height + 1):
        if (item + 2) % 2 == 0:
            print(width * (' *'))
        else:
            print(width * ('* '))


if __name__ == '__main__':
    get_board()
