#Diese Datei enthält die Methoden für die Suchalgorithmen sowie einige Hilfsfunktionen.
#Konkret soll ein Weg von links oben nach rechts unten gefunden werden, der alle Hindernisse meidet.
#Die Koordinaten dieser Hindernisse werden der Funktion als Liste von Paaren übergeben.
#Ausgabe ist ein Generator, in dem jeder Eintrag einen Schritt des Algorithmus darstellt.
#Ein Eintrag ist dabei ein Tupel von zwei Listen, wobei die erste alle bisher besuchten Felder enthält
#und die zweite Liste alle Felder, die zum aktuellen Pfad gehören.

def DFS(obstacles):
    size=20
    visited=[(0,0)]
    predecessors=[[(0,0) for i in range(size)] for j in range(size)]
    to_be_visited=find_neighbors(0,0,size,obstacles+visited)
    while to_be_visited!=[]:
        point=to_be_visited.pop(0)
        if point==(size-1,size-1):
            break
        if point in visited:
            continue
        visited.append(point)
        new_goals=find_neighbors(point[0],point[1],size,obstacles+visited)
        to_be_visited=new_goals+to_be_visited
        for i,j in new_goals:
            if (i,j) not in visited:
                predecessors[i][j]=point
        path=find_path(point,predecessors)
        yield (visited,path)

def BFS(obstacles):
    size=20
    visited=[(0,0)]
    predecessors=[[(0,0) for i in range(size)] for j in range(size)]
    to_be_visited=find_neighbors(0,0,size,obstacles+visited)
    while to_be_visited!=[]:
        point=to_be_visited.pop(len(to_be_visited)-1)
        if point in visited:
            continue
        visited.append(point)
        new_goals=find_neighbors(point[0],point[1],size,obstacles+visited)
        to_be_visited=new_goals+to_be_visited
        for i,j in new_goals:
            if (i,j) not in visited:
                predecessors[i][j]=point
        path=find_path(point,predecessors)
        yield (visited,path)
        if point==(size-1,size-1):
            break

#Diese Funktion gibt eine Liste von Koordinatenpaaren aus, wobei die zugehörigen Felder, den Weg von oben
#Links zum übergebenen Feld point enthalten. predecessors ist dabei eine zweidimensionale Liste,
#die zu jedem bereits besuchten Feld die Koordinaten des Feldes enthält, von dem aus es erreicht wurde.       
def find_path(point,predecessors):
    path=[]
    while point!=(0,0):
        path.append(point)
        point=predecessors[point[0]][point[1]]
    return path

#Gibt innerhalb eines quadratischen Gitters mit Kantenlänge size die Koordinaten von allen Nachbarfeldern
#von (i,j) zurück, die nicht in der Liste obstacles stehen.
def find_neighbors(i,j,size,obstacles):
    neighbors=[]
    if i<size-1 and not (i+1,j) in obstacles:
        neighbors.append((i+1,j))
    if j<size-1 and not (i,j+1) in obstacles:
        neighbors.append((i,j+1))
    if i>0 and not (i-1,j) in obstacles:
        neighbors.append((i-1,j))
    if j>0 and not (i,j-1) in obstacles:
        neighbors.append((i,j-1))
    return neighbors