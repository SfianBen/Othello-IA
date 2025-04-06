import copy
from evaluation import Evaluation
from dummy import DummyBoard
from logic import GameLogic

class MinMaxAI:
    def __init__(self, color, depth=3, evaluation="score"):
        self.color = color
        self.depth = depth
        self.evaluation = evaluation

    def evaluate(self, logic):
        if self.evaluation == "score":
            return Evaluation.by_score(logic.board.board, self.color)
        elif self.evaluation == "position":
            return Evaluation.by_position(logic.board.board, self.color)
        elif self.evaluation == "mobilité":
            return Evaluation.by_mobility(logic, self.color)
        else:
            return Evaluation.mixed(logic, self.color)

    def get_opponent_color(self):
        return "W" if self.color == "B" else "B"

    def get_best_move(self, game_logic):
        best_score = float('-inf')
        best_move = None
        for move in game_logic.get_valid_moves(self.color):
            board_copy = DummyBoard(copy.deepcopy(game_logic.board.board))
            logic_copy = GameLogic(board_copy)
            logic_copy.apply_move(*move, self.color)
            score = self.minmax(logic_copy, self.depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minmax(self, logic, depth, maximizing):
        color = self.color if maximizing else self.get_opponent_color()
        moves = logic.get_valid_moves(color)
        if depth == 0 or not moves:
            return self.evaluate(logic)
        scores = []
        for move in moves:
            board_copy = DummyBoard(copy.deepcopy(logic.board.board))
            logic_copy = GameLogic(board_copy)
            logic_copy.apply_move(*move, color)
            score = self.minmax(logic_copy, depth - 1, not maximizing)
            scores.append(score)
        return max(scores) if maximizing else min(scores)
