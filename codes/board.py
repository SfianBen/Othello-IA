import tkinter as tk

CELL_SIZE = 60
BOARD_SIZE = 8

class OthelloBoard(tk.Canvas):
    def __init__(self, master, on_click_case):
        super().__init__(master, width=CELL_SIZE*BOARD_SIZE, height=CELL_SIZE*BOARD_SIZE, bg="darkgreen")
        self.on_click_case = on_click_case
        self.bind("<Button-1>", self.handle_click)
        self.board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.init_board()
        self.draw_board()

    def init_board(self):
        self.board[3][3] = "W"
        self.board[4][4] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"

    def handle_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        self.on_click_case(row, col)

    def draw_board(self):
        self.delete("all")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.create_rectangle(x1, y1, x2, y2, outline="black")
                if self.board[i][j] == "B":
                    self.create_oval(x1+5, y1+5, x2-5, y2-5, fill="black")
                elif self.board[i][j] == "W":
                    self.create_oval(x1+5, y1+5, x2-5, y2-5, fill="white")

    def reset_board(self):
        self.board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.init_board()
        self.draw_board()
