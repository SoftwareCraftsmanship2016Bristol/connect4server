"""
Board code?
"""

winner_sets = {}
MAX_COLS = 7
MAX_ROWS = 6
CONNECT_NUM = 4

connect_window = CONNECT_NUM - 1

for column in range(MAX_COLS):
    right = min(MAX_COLS - 1,column + connect_window)
    left = max(0, column - connect_window)
    for row in range(MAX_ROWS):
        above = min(MAX_ROWS - 1, connect_window)
        below = max(0, connect_window)
        # Enumerate winning conditions
        combinations = []
        offset = 0
        horizontal = right - left - connect_window + 1

        for start_col in range(left, left+horizontal):
            combinations.append(
                [(c, row) for c in range(start_col, start_col+CONNECT_NUM)])

        vertical = above - below - connect_window + 1
        for start_row in range(below, below+vertical):
            combinations.append([(col, r) for r in range(start_row, start_row+CONNECT_NUM)])

        # TODO: Positive diagonal
        # TODO: Negative diagonal



class Board(dict):

    board_columns = 7

    def __init__(self):
        super().__init__(self)
        for i in range(self.board_columns):
            self[i] = [0] * 6

        self.win = False

    def MakeMove(self, column, player = 1):
        column = column-1
        first_zero = self[column].index(0)
        self[column][first_zero] = player
        self.latest_move = column, row
        self.CheckWinningMove()
        return self

    def CheckWinningMove(self):
        self._checkVerticalWin()
        self._checkHorizontalWin()
        self._checkDiagonalWin()

    def _checkVerticalWin(self):
        if self[0][:4] == [1,1,1,1]:
            self.win = True

    def _checkHorizontalWin(self):
        for i in range(4):
            if self[i][0] != 1:
                break
        else:
            self.win = True

    def _checkDiagonalWin(self):
        column, row = self.latest_move

        for i in range(4):
            if self[i][i] != 1:
                break
        else:
            self.win = True
