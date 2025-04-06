import copy
from evaluation import Evaluation
from dummy import DummyBoard
from logic import GameLogic

class AlphaBetaAI:
    def __init__(self, color, depth=3, evaluation='score'):
        self.color = color
        self.depth = depth
        self.eval_method = evaluation

    def evaluate(self, logic):
        if self.eval_method == 'score':
            return Evaluation.by_score(logic.board.board, self.color)
        elif self.eval_method == 'position':
            return Evaluation.by_position(logic.board.board, self.color)
        elif self.eval_method == 'mobilité':
            return Evaluation.by_mobility(logic, self.color)
        else:
            return Evaluation.mixed(logic, self.color)

    def get_opponent_color(self):
        return 'W' if self.color == 'B' else 'B'

    def get_best_move(self, game_logic):
        best_score = float('-inf')
        best_move = None
        for move in game_logic.get_valid_moves(self.color):
            test_board = DummyBoard(copy.deepcopy(game_logic.board.board))
            test_logic = GameLogic(test_board)
            test_logic.apply_move(*move, self.color)
            score = self.alphabeta(test_logic, self.depth - 1, float('-inf'), float('inf'), False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def alphabeta(self, logic, depth, alpha, beta, maximizing):
        color = self.color if maximizing else self.get_opponent_color()
        valid_moves = logic.get_valid_moves(color)
        if depth == 0 or not valid_moves:
            return self.evaluate(logic)

        if maximizing:
            max_eval = float('-inf')
            for move in valid_moves:
                temp_board = DummyBoard(copy.deepcopy(logic.board.board))
                temp_logic = GameLogic(temp_board)
                temp_logic.apply_move(*move, color)
                eval = self.alphabeta(temp_logic, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in valid_moves:
                temp_board = DummyBoard(copy.deepcopy(logic.board.board))
                temp_logic = GameLogic(temp_board)
                temp_logic.apply_move(*move, color)
                eval = self.alphabeta(temp_logic, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
