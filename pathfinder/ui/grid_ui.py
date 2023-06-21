import tkinter as tk
from pathfinder.data_structure.map import Map
from pathfinder.shortcuts import *
from pathfinder.engines.search import RandomWalk
import time

class GridUI(): 

    def __init__(self, rows:int, cols:int) -> None:
        self.rows = rows
        self.cols = cols       
        self.map = Map(self.rows, self.cols)
        self.window = tk.Tk()
        self.frames = [[None for _ in range(self.cols )] for _ in range(self.rows)]
        

    def draw_map(self): 
        self.window.configure(bg="black")
        # create map 

        for row in range(self.rows):
            self.window.rowconfigure(self.rows, weight=1)  
            for col in range(self.cols):
                self.window.columnconfigure(self.cols, weight=1)
                frame = tk.Frame(
                    master=self.window,
                    relief=tk.RAISED,
                    borderwidth=1,
                    width=100,
                    height=100,
                    bg="#444444"
                )
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                # Associazione della funzione di callback al clic del mouse
                frame.bind("<Button-1>", self.cell_clicked)
                self.frames[row][col] = frame
            
        ok_buttom = tk.Button(self.window, text="OK", command= self.random_walk)
        ok_buttom.grid(row=self.rows, columnspan=self.cols, pady=10)

    def cell_clicked(self, event):
        # Ottieni la coordinata della cella cliccata
        cell_widget = event.widget
        i = cell_widget.grid_info()['row']
        j = cell_widget.grid_info()['column']
        
        if self.map.start is None: 
            self.map.insert_element((i,j), START)
            cell_widget.configure(bg="green")
        elif self.map.end is None: 
            self.map.insert_element((i,j), END)
            cell_widget.configure(bg="blue")
        else: 
            self.map.insert_element((i,j), OBSTACLE)
            cell_widget.configure(bg="black")

    def random_walk(self):
        random_walk = RandomWalk(self.map)
        solution = random_walk.solve()
        colored_before = None

        delta = 0
        for i,j in solution: 
            delta += 100
            if colored_before is not None:
                tmp_i, tmp_j = colored_before
                self.window.after(delta, lambda tmp_i=tmp_i, tmp_j=tmp_j: self.frames[tmp_i][tmp_j].config(bg="#444444") )
            colored_before = (i,j)
            self.window.after(delta, lambda i=i, j=j: self.frames[i][j].config(bg="red") )
      
            
        
        


    



    

    