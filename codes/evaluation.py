POSITION_WEIGHTS = [
    [100, -20, 10, 5, 5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100]
]

class Evaluation:
    @staticmethod
    def by_score(board, color):
        score = 0
        for row in board:
            for cell in row:
                if cell == color:
                    score += 1
                elif cell != " ":
                    score -= 1
        return score

    @staticmethod
    def by_position(board, color):
        opp = "W" if color == "B" else "B"
        score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == color:
                    score += POSITION_WEIGHTS[i][j]
                elif board[i][j] == opp:
                    score -= POSITION_WEIGHTS[i][j]
        return score

    @staticmethod
    def by_mobility(logic, color):
        opp = "W" if color == "B" else "B"
        return len(logic.get_valid_moves(color)) - len(logic.get_valid_moves(opp))

    @staticmethod
    def mixed(logic, color):
        return (Evaluation.by_score(logic.board.board, color)
                + Evaluation.by_position(logic.board.board, color)
                + 10 * Evaluation.by_mobility(logic, color))
