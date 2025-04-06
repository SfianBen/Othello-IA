import tkinter as tk
from game import OthelloGame

class OthelloMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Othello IA")
        self.master.geometry("400x450")
        self.build_menu()

    def build_menu(self):
        tk.Label(self.master, text="Mode de jeu :", font=("Helvetica", 14)).pack(pady=10)
        self.mode_var = tk.StringVar(value="PvIA")
        tk.Radiobutton(self.master, text="Joueur vs IA", variable=self.mode_var, value="PvIA").pack()
        tk.Radiobutton(self.master, text="IA vs IA", variable=self.mode_var, value="IAvIA").pack()

        tk.Label(self.master, text="Algorithme IA :", font=("Helvetica", 14)).pack(pady=10)
        self.ia_var = tk.StringVar(value="MinMax")
        for algo in ["MinMax", "AlphaBeta", "NegaMax"]:
            tk.Radiobutton(self.master, text=algo, variable=self.ia_var, value=algo).pack()

        tk.Label(self.master, text="Méthode d’évaluation :", font=("Helvetica", 14)).pack(pady=10)
        self.eval_var = tk.StringVar(value="score")
        for eval_type in ["score", "position", "mobilité", "mixte"]:
            tk.Radiobutton(self.master, text=eval_type.capitalize(), variable=self.eval_var, value=eval_type).pack()

        tk.Button(self.master, text="Lancer la partie", font=("Helvetica", 12), command=self.start_game).pack(pady=20)

    def start_game(self):
        mode = self.mode_var.get()
        algo = self.ia_var.get()
        evaluation = self.eval_var.get()
        self.master.destroy()

        root = tk.Tk()
        root.title("Jeu Othello")

        if mode == "PvIA":
            OthelloGame(root, player_color="B", ia_algo=algo, eval_method=evaluation)
        else:
            OthelloGame(root, player_color=None, ia_algo=algo, eval_method=evaluation)

        root.mainloop()
