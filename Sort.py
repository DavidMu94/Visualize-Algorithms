#Jede der Methoden in dieser Datei führt einen Sortieralgorithmus aus.
#Eingabe ist dabei eine Liste von Dezimalzahlen, die sortiert werden soll.
#Ausgabe ist ein Generator, in dem jeder Eintrag einen Schritt des Algorithmus darstellt.
#Ein Eintrag ist dabei ein Tupel von zwei Listen, wobei die erste den Zwischenstand der zu
#sortierenden Liste nach dem jeweiligen Schritt angibt. Die zweite Liste enthält die Indizes der
#für diesen Schritt wichtigen Einträge, die grafisch hervorgehoben werden sollen; diese zweite
#Liste kann leer sein.

def bubblesort(values):
    n=len(values)
    for i in range(n,1,-1):
        for j in range(0,i-1):
            if values[j]>values[j+1]:
                values[j],values[j+1]=values[j+1],values[j]
            yield values,[j,j+1]

#Die zusätzlichen Parameter start und end dienen dazu, die Rekursion im Algorithmus zu ermöglichen.
#Wenn der Algorithmus von außen aufgerufen wird, können hier immer die vorgegebenen Werte verwendet werden.
def mergesort(values,start=0,end=None):
    if end is None:
        end=len(values)
    n=end-start
    if n==1:
        yield values,[start]
    else:
        yield from mergesort(values,start,start+n//2)
        yield from mergesort(values,start+n//2,end)
        neu=[]
        ind_links=start
        ind_rechts=start+n//2
        for i in range(n):
            if ind_rechts==end or (ind_links<start+n//2 and values[ind_links]<values[ind_rechts]):
                neu.append(values[ind_links])
                ind_links+=1
            else:
                neu.append(values[ind_rechts])
                ind_rechts+=1
        values[start:end]=neu
        yield values,list(range(start,end))

#Die zusätzlichen Parameter start und end dienen dazu, die Rekursion im Algorithmus zu ermöglichen.
#Wenn der Algorithmus von außen aufgerufen wird, können hier immer die vorgegebenen Werte verwendet werden.
def quicksort(values,start=0,end=None):
    if end is None:
        end=len(values)
    n=end-start
    if n>1:
        yield values,list(range(start,end))
        pivot=values[start+n//2]
        yield values,[start+n//2]
        left=[v for v in values[start:end] if v<pivot]
        right=[v for v in values[start:end] if v >pivot]
        m=len(left)
        values[start:end]=left+[pivot]+right
        yield values,[start+m]
        yield from quicksort(values,start,start+m)
        yield from quicksort(values,start+m+1,end)