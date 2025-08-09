class Backgammon:
    def __init__(self):
        self.board: list[int] = []

        self.initialize_board()

    def initialize_board(self):
        self.board = [2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0,0 -2]

    def print_board(self):
        print(self.board)