import time
import tkinter as tk
from tkinter import messagebox
from board import OthelloBoard
from logic import GameLogic
from ai_minmax import MinMaxAI
from ai_alphabeta import AlphaBetaAI
from ai_negamax import NegaMaxAI

class OthelloGame:
    def __init__(self, root, player_color="B", ia_algo="MinMax", eval_method="score"):
        self.root = root
        self.player_color = player_color
        self.ia_algo = ia_algo
        self.eval_method = eval_method
        self.ia_color = "W" if player_color == "B" else "B" if player_color == "W" else None
        self.turn = "B"
        self.turn_count = 1
        self.start_time = time.time()

        self.board_ui = OthelloBoard(root, self.handle_click)
        self.board_ui.pack()

        self.logic = GameLogic(self.board_ui)
        self.ai_black = self.create_ai("B") if player_color is None else None
        self.ai_white = self.create_ai("W")

        self.status_label = tk.Label(root, font=("Helvetica", 14))
        self.status_label.pack()

        self.timer_label = tk.Label(root, font=("Helvetica", 12))
        self.timer_label.pack()

        self.replay_button = tk.Button(root, text="Rejouer", command=self.restart_game)
        self.replay_button.pack(pady=10)

        self.update_status()
        self.tick_timer()

        if self.player_color is None or self.turn == self.ia_color:
            self.root.after(500, self.ai_move)

    def create_ai(self, color):
        if self.ia_algo == "MinMax":
            return MinMaxAI(color, 3, self.eval_method)
        elif self.ia_algo == "AlphaBeta":
            return AlphaBetaAI(color, 3, self.eval_method)
        else:
            return NegaMaxAI(color, 3, self.eval_method)

    def handle_click(self, row, col):
        if self.player_color is None or self.turn != self.player_color:
            return
        if self.logic.apply_move(row, col, self.player_color):
            self.next_turn()

    def ai_move(self):
        current_ai = self.ai_black if self.turn == "B" else self.ai_white
        if current_ai:
            move = current_ai.get_best_move(self.logic)
            if move:
                self.logic.apply_move(*move, self.turn)
                #  Écriture dans un fichier
                eval_score = current_ai.evaluate(self.logic) if self.ia_algo != "NegaMax" else current_ai.evaluate(self.logic, self.turn)
                with open("evaluation_log.txt", "a") as f:
                    f.write(f"Tour {self.turn_count} | IA ({self.turn}) | evaluation {self.eval_method} : {eval_score}\n")
        self.next_turn()


    def next_turn(self):
        self.turn_count += 1
        self.turn = "W" if self.turn == "B" else "B"
        self.update_status()

        #  Fin automatique si le plateau est plein
        if all(cell != " " for row in self.logic.board.board for cell in row):
            self.end_game()
            return

        # Vérifie s'il y a des coups valides, sinon alterne, sinon fin
        if not self.logic.get_valid_moves(self.turn):
            self.turn = "W" if self.turn == "B" else "B"
            if not self.logic.get_valid_moves(self.turn):
                self.end_game()
                return

        if self.player_color is None or self.turn == self.ia_color:
            self.root.after(500, self.ai_move)

    def update_status(self):
        b, w = self.logic.count_score()
        self.status_label.config(
            text=f"Tour: {self.turn_count} | Score – Noir (B): {b}  Blanc (W): {w} | Joueur actuel: {self.turn}"
        )

    def tick_timer(self):
        elapsed = int(time.time() - self.start_time)
        mins, secs = divmod(elapsed, 60)
        self.timer_label.config(text=f"Temps écoulé: {mins:02d}:{secs:02d}")
        self.root.after(1000, self.tick_timer)

    def restart_game(self):
        self.turn = "B"
        self.turn_count = 1
        self.start_time = time.time()
        self.board_ui.reset_board()
        self.logic = GameLogic(self.board_ui)
        self.ai_black = self.create_ai("B") if self.player_color is None else None
        self.ai_white = self.create_ai("W")
        self.update_status()
        if self.player_color is None or self.turn == self.ia_color:
            self.root.after(500, self.ai_move)

    def end_game(self):
        b, w = self.logic.count_score()
        if b > w:
            msg = "Victoire des Noirs (B) !"
        elif w > b:
            msg = "Victoire des Blancs (W) !"
        else:
            msg = "Match nul !"
        messagebox.showinfo("Fin de partie ;)", msg)

