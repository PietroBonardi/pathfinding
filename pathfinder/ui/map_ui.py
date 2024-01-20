import tkinter as tk
from pathfinder.data_structure.map import Map
from pathfinder.shortcuts import *
from pathfinder.engines.search import RandomWalk, DepthFirstSearch
from typing import List, Tuple
import time


class MapUI: 
    # TODO: add solver parameter 
    def __init__(self, rows:int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        # gap between logic and ui
        self.window = tk.Tk()
        self.frames = [[None for _ in range(self.cols)]
                       for _ in range(self.rows)]
        self.map = Map(rows, cols)
        self.solver = None

    def create_map(self):
        for row in range(self.rows):
            for col in range(self.cols):
                frame = tk.Frame(self.window, width=100, height=100, bg="grey")
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                frame.bind("<Button-1>", self.on_button_click)
                self.frames[row][col] = frame
        
        clear = tk.Button(self.window, text="clear", command=self.clear)
        clear.grid(row=self.rows, column=self.cols-1, padx=10, pady=20)

        run = tk.Button(self.window, text="run", command=self.run)
        run.grid(row=self.rows, column=0, padx=10, pady=10)

   
    def on_button_click(self, event) -> None: 
        cell_widget = event.widget
        row = cell_widget.grid_info()['row']
        col = cell_widget.grid_info()['column']

        if self.map.start is None: 
            self.map.insert_element((row,col), label=START)
            cell_widget.config(bg="blue")

        elif self.map.end is None: 
            self.map.insert_element((row,col), label=END)
            cell_widget.config(bg="red")

        else: 
            self.map.insert_element((row,col), label=OBSTACLE)
            cell_widget.config(bg="black")
    
    def clear(self) -> None:
        self.map.start, self.map.end = None, None
        for i in range(self.rows):
            for j in range(self.cols):
                self.frames[i][j].config(bg="grey")

    def draw_solution(self, solution: list[Tuple[int,int]]) -> None: 
        colored_before = None
        delay = 0
        start = solution[0]
        end = solution[-1]

        for i, j in solution:
            if (i,j) != start and (i,j) != end:
                delay+=50
                self.window.after(delay, lambda i = i, j = j : self.frames[i][j].config(bg="white"))
                if colored_before:
                    tmp_i, tmp_j = colored_before
                    self.window.after(delay, lambda tmp_i = tmp_i, tmp_j = tmp_j : self.frames[tmp_i][tmp_j].config(bg="gray"))
                
                colored_before = (i,j)
        
        self.window.after(delay, lambda tmp_i = colored_before[0], tmp_j = colored_before[1] : self.frames[tmp_i][tmp_j].config(bg="gray"))
        self.window.after(delay, lambda tmp_i = i, tmp_j = j : self.frames[tmp_i][tmp_j].config(bg="yellow"))


    # NOTE: bug when using chess map disposition!
    def run(self) -> None:
        # TODO: add solver
        self.solver = DepthFirstSearch(self.map)
        self.draw_solution(self.solver.solve())


