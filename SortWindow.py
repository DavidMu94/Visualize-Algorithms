from tkinter import *
import random
import copy
import Sort
from MainWindow import *

class SortWindow(MainWindow):
    def __init__(self,root):
        MainWindow.__init__(self,root)

    def create(self):
        self.timestep=500
        self.algorithms={"Bubblesort":Sort.bubblesort,"Mergesort":Sort.mergesort,"Quicksort":Sort.quicksort}
        self.algorithm=Sort.bubblesort
        self.startValues=[random.random() for i in range(20)]
        self.input=copy.copy(self.startValues)
        self.rects=[]
        for i in range(20):
            self.rects.append(self.canvas.create_rectangle(10*(i+1),(1-self.startValues[i])*200+10,10*(i+2),210,fill="green"))

    def update_timestep(self):
        if self.algorithm==Sort.bubblesort:
            self.timestep=200
        else:
            self.timestep=500

    def reset(self):
        self.input=copy.copy(self.startValues)
        self.redraw((self.startValues,[]))
    
    #Darstellen eines neuen Schritts auf dem Bildschirm; step bezeichnet hierbei die Daten, die die
    #Funktion vom Algorithmus für diesen Schritt liefert.
    def redraw(self,step):
        v,f=step
        for j in range(20):
            self.canvas.coords(self.rects[j],10*(j+1),(1-v[j])*200+10,10*(j+2),210)
            if j in f:
                self.canvas.itemconfig(self.rects[j],fill="red")
            else:
                self.canvas.itemconfig(self.rects[j],fill="green")