#Das Hauptfenster, in dem die Darstellung der Algorithmen abläuft. Für die verschiedenen Probleme
#gibt es jeweils eine Subklasse dieser Klasse, die die für das Problem spezifischen Teile enthält.

from tkinter import *

class MainWindow(Tk):
    def __init__(self,root):
        Tk.__init__(self)
        self.root=root
        self.status=0 #0: Algorithmus nicht gestartet, 1: Algorithmus läuft, 2: Algorithmus ist pausiert,
                        #3: Algorithmus ist beendet.
        self.instruction=Label(self,text="Bitte wählen Sie den gewünschten \n \
Algorithmus aus.")
        self.instruction.pack()
        self.canvas=Canvas(self,width=220,height=220)
        self.create()
        self.algorithmChoice=Listbox(self,height=0)
        for a in self.algorithms.keys():
            self.algorithmChoice.insert("end",a)
        self.algorithmChoice.pack()
        self.canvas.pack()
        self.buttonStart=Button(self,text="Starten",command=lambda:self.start(),width=15,height=2)
        self.buttonStart.pack()
        self.buttonPause=Button(self,text="Pause",command=lambda:self.pause(),width=15,height=2)
        self.buttonPause.pack()
        self.buttonBack=Button(self,text="Zurück",command=lambda:self.goBack(),width=10,height=2)
        self.buttonBack.pack()

    #Diese Methode enthält das, was passieren soll, wenn der Nutzer auf den Pause-Button klickt,
    #auch dann, wenn dieser gerade mit Fortsetzen beschriftet ist.
    def pause(self):
        if self.status==1:
            self.status=2
            self.buttonPause.configure(text="Fortsetzen")
        elif self.status==2:
            self.status=1
            self.buttonPause.configure(text="Pause")
            self.showSteps()

    #Diese Methode enthält das, was passieren soll, wenn der Nutzer auf den Start-Button klickt,
    #auch dann, wenn dieser gerade mit Neu Starten beschriftet ist.
    def start(self):
        if self.status==0:
            self.status=1
            try:
                self.algorithm=self.algorithms[self.algorithmChoice.get("active")]
            except:
                pass
            self.update_timestep()
            self.steps=self.algorithm(self.input)
            self.buttonStart.configure(text="Neu Starten")
            self.showSteps()
        elif self.status in [1,2,3]:
            if self.status==2:
                self.buttonPause.configure(text="Pause")
            self.status=0
            self.buttonStart.configure(text="Starten")
            self.reset()

    #Schließt dieses Fenster; das Programm kehrt zum Startfenster zurück.   
    def goBack(self):
        self.root.deiconify()
        self.destroy()

    #Beendet das gesamte Programm.
    def endProgram(self):
        self.root.destroy()
        self.destroy()

    #Veranlasst, dass der nächste Schritt gezeichnet wird, sofern der Status gleich 1 ist und der Algorithmus
    #noch nicht am Ende angekommen ist. In letzterem Fall wird der Status auf 3 gesetzt.
    #Nach Ablauf des Timestep ruft sich die Methode wieder selbst auf.
    def showSteps(self):
        if self.status==1:
            try:
                step=next(self.steps)
                self.redraw(step)
                self.after(self.timestep,self.showSteps)
            except:
                self.status=3