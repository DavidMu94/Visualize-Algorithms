#Diese Datei startet das ganze Programm. Sie enthält die Klasse für das Startfenster, aus dem heraus die
#Fenster zu den einzelnen Problemen (Suchen, Sortieren) aufgerufen werden können.

from tkinter import *
import SortWindow
import SearchWindow

class StartWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.instruction=Label(self,text="Bitte wählen Sie das Problem aus, \n \
zu dem Sie Lösungsalgorithmen sehen wollen.")
        self.instruction.pack()
        self.buttonSort=Button(self,text="Sortieren", 
         command=lambda:self.openProblemWindow(SortWindow.SortWindow), width=15, height=3)
        self.buttonSort.pack()
        self.buttonSearch=Button(self,text="Suchen",
         command=lambda:self.openProblemWindow(SearchWindow.SearchWindow), width=15, height=3)
        self.buttonSearch.pack()
        self.buttonEnd=Button(self,text="Programm\nbeenden",
         command=self.destroy,width=10,height=2)
        self.buttonEnd.pack()

    #Diese Methode öffnet ein neues Fenster von der Klasse, die durch den Parameter window übergeben wird,
    #und schließt außerdem das aktuelle Fenster.
    def openProblemWindow(self,window):
        b=window(self)
        #Wenn das neue Fenster geschlossen wird, soll auch das Startfenster endgültig beendet werden.
        b.protocol("WM_DELETE_WINDOW",b.endProgram)
        self.withdraw()
        b.mainloop()

start=StartWindow()
start.mainloop()