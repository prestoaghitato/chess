#!/usr/bin/env python3
import tkinter as tk

GRID_COLOR = "#A39489"
EMPTY_CELL_COLOR = "#C2B3A9"
SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT = ("Helvetica", 36, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_OVER_FONT_COLOR = "#FFFFFF"
WINNER_BG= "#FFCC00"
LOSER_BG = "#A39489"

CELL_COLORS = {
    2:    "#FCEFE6",
    4:    "#F2E8CB",
    8:    "#F5B682",
    16:   "#F29446",
    32:   "#FF775C",
    64:   "#E64C2E",
    128:  "#EDE291",
    256:  "#FCE130",
    512:  "#FFDB4A",
    1024: "#F0B922",
    2048: "#FAD74D",
}

CELL_NUMBER_COLORS = {
    2:    "#695C57",
    4:    "#695C57",
    8:    "#FFFFFF",
    16:   "#FFFFFF",
    32:   "#FFFFFF",
    64:   "#FFFFFF",
    128:  "#FFFFFF",
    256:  "#FFFFFF",
    512:  "#FFFFFF",
    1024: "#FFFFFF",
    2048: "#FFFFFF",
}

CELL_NUMBER_FONTS = {
    2:    ("Helvetica", 55, "bold"),
    4:    ("Helvetica", 55, "bold"),
    8:    ("Helvetica", 55, "bold"),
    16:   ("Helvetica", 50, "bold"),
    32:   ("Helvetica", 50, "bold"),
    64:   ("Helvetica", 50, "bold"),
    128:  ("Helvetica", 45, "bold"),
    256:  ("Helvetica", 45, "bold"),
    512:  ("Helvetica", 45, "bold"),
    1024: ("Helvetica", 40, "bold"),
    2048: ("Helvetica", 40, "bold"),
}

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        # gui outline is 4x4 grid
        self.main_grid = tk.Frame(
            self,
            bg=GRID_COLOR,
            bd=3,
            width=600,
            height=600,
        )
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.mainloop()

    def make_GUI(self):
        # make grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=EMPTY_CELL_COLOR,
                    width=150,
                    height=150,
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # make score header
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, rely=45, anchor="center")
        tk.Label(score_frame, text="Score", font=SCORE_LABEL_FONT).grid(row=0)
        self.score_label = tk.Label(score_frame, tex="0", font=SCORE_FONT)
        self.score_label.grid(row=1)

Game()
