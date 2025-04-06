import copy
from evaluation import Evaluation
from dummy import DummyBoard
from logic import GameLogic

class NegaMaxAI:
    def __init__(self, color, depth=3, evaluation='score'):
        self.color = color
        self.depth = depth
        self.eval_method = evaluation

    def evaluate(self, logic, color):
        if self.eval_method == 'score':
            return Evaluation.by_score(logic.board.board, color)
        elif self.eval_method == 'position':
            return Evaluation.by_position(logic.board.board, color)
        elif self.eval_method == 'mobilité':
            return Evaluation.by_mobility(logic, color)
        else:
            return Evaluation.mixed(logic, color)

    def get_opponent_color(self, color):
        return 'W' if color == 'B' else 'B'

    def get_best_move(self, game_logic):
        best_score = float('-inf')
        best_move = None
        for move in game_logic.get_valid_moves(self.color):
            test_board = DummyBoard(copy.deepcopy(game_logic.board.board))
            test_logic = GameLogic(test_board)
            test_logic.apply_move(*move, self.color)
            score = -self.negamax(test_logic, self.depth - 1, self.get_opponent_color(self.color))
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def negamax(self, logic, depth, color):
        valid_moves = logic.get_valid_moves(color)
        if depth == 0 or not valid_moves:
            return self.evaluate(logic, color)

        max_score = float('-inf')
        for move in valid_moves:
            temp_board = DummyBoard(copy.deepcopy(logic.board.board))
            temp_logic = GameLogic(temp_board)
            temp_logic.apply_move(*move, color)
            score = -self.negamax(temp_logic, depth - 1, self.get_opponent_color(color))
            max_score = max(max_score, score)
        return max_score
