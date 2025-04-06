BOARD_SIZE = 8
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1),  (1, 0), (1, 1)]

class GameLogic:
    def __init__(self, board):
        self.board = board

    def get_valid_moves(self, color):
        moves = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board.board[i][j] == " " and self._would_flip(i, j, color):
                    moves.append((i, j))
        return moves

    def _would_flip(self, row, col, color):
        opp = "W" if color == "B" else "B"
        for dx, dy in DIRECTIONS:
            r, c = row + dx, col + dy
            path = []
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board.board[r][c] == opp:
                path.append((r, c))
                r += dx
                c += dy
            if path and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board.board[r][c] == color:
                return True
        return False

    def apply_move(self, row, col, color):
        if not self._would_flip(row, col, color):
            return False
        opp = "W" if color == "B" else "B"
        self.board.board[row][col] = color
        for dx, dy in DIRECTIONS:
            r, c = row + dx, col + dy
            path = []
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board.board[r][c] == opp:
                path.append((r, c))
                r += dx
                c += dy
            if path and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board.board[r][c] == color:
                for pr, pc in path:
                    self.board.board[pr][pc] = color
        self.board.draw_board()
        return True

    def count_score(self):
        b = sum(row.count("B") for row in self.board.board)
        w = sum(row.count("W") for row in self.board.board)
        return b, w
