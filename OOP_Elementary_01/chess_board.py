"""
The program displays a chessboard with the given dimensions
of height and width, according to the following principle:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
"""


class ChessBoard:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def get_chess_board(self):
        for item in range(1, self.height + 1):
            if (item + 2) % 2 == 0:
                print(self.width * ' *')
            else:
                print(self.width * '* ')


if __name__ == '__main__':
    while True:
        try:
            height = int(input("Enter the height of the picture: "))
            width = int(input("Enter the width of the picture: "))
            break
        except ValueError:
            print("Please, input the correct values! ")

    board = ChessBoard(height, width)
    board.get_chess_board()
