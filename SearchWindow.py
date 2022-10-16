from tkinter import *
import random
import Search
from MainWindow import *

class SearchWindow(MainWindow):
    def __init__(self,root):
        MainWindow.__init__(self,root)

    def create(self):
        self.timestep=200
        self.algorithms={"Tiefensuche":Search.DFS,"Breitensuche":Search.BFS}
        self.algorithm=Search.DFS
        self.obstacles=[]
        counter=0
        while(counter<100):
            i=random.randint(0,19)
            j=random.randint(0,19)
            if not ((i,j)==(0,0) or (i,j)==(19,19) or (i,j) in self.obstacles):
                self.obstacles.append((i,j))
                counter+=1
        self.input=self.obstacles
        self.squares=[[] for i in range(20)]
        for i in range(20):
            for j in range(20):
                if (i,j)==(0,0) or (i,j)==(19,19):
                    self.squares[i].append(self.canvas.create_rectangle(10*(i+1),10*(j+1),10*(i+2),10*(j+2),fill="red"))
                elif (i,j) in self.obstacles:
                    self.squares[i].append(self.canvas.create_rectangle(10*(i+1),10*(j+1),10*(i+2),10*(j+2),fill="black"))
                else:
                    self.squares[i].append(self.canvas.create_rectangle(10*(i+1),10*(j+1),10*(i+2),10*(j+2),fill="blue"))

    def update_timestep(self):
        self.timestep=200

    def reset(self):
        self.redraw(([],[]))
    
    #Darstellen eines neuen Schritts auf dem Bildschirm; step bezeichnet hierbei die Daten, die die
    #Funktion vom Algorithmus für diesen Schritt liefert.
    def redraw(self,step):
        visited=step[0]
        path=step[1]
        for i in range(20):
            for j in range(20):
                if (i,j)==(0,0) or (i,j)==(19,19) or (i,j) in self.obstacles:
                    continue
                if (i,j) in path:
                    self.canvas.itemconfig(self.squares[i][j],fill="green")
                elif (i,j) in visited:
                    self.canvas.itemconfig(self.squares[i][j],fill="yellow")
                else:
                    self.canvas.itemconfig(self.squares[i][j],fill="blue")