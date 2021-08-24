
import random

def updatePosition(n, m, pos, rnd):

    if pos >= 0 and pos <= (n*m-1):
        rowlists = []                                       # rowlists: list

        for i in range(0, n):
            rowlists.append([p for p in range(i*m, (i+1)*m)])
            # append an Liste
            if pos in range(i*m, (i+1)*m):                  # Liste von pos
                listnumber = i
                listposition = pos % m                      # Pos. von pos

        if rnd >= 0 and rnd < 0.25:                         # ->
            if pos+1 in rowlists[listnumber]:
                L = pos+1
            else:
                L = rowlists[listnumber][0]

        if rnd >= 0.25 and rnd < 0.5:                       # <-
            if pos-1 in rowlists[listnumber]:
                L = pos-1
            else:
                L = rowlists[listnumber][m-1]

        if rnd >= 0.5 and rnd < 0.75:                       # unten
            if listnumber < n-1:
                L = rowlists[listnumber+1][listposition]
            else:
                L = rowlists[0][listposition]

        if rnd >= 0.75 and rnd < 1:                         # oben
            if listnumber > 0:
                L = rowlists[listnumber-1][listposition]
            else:
                L = rowlists[n-1][listposition]

        return L                                            # L: integer


def updatePositions(n, m, positions):                       # pos geupdatet

    for i in range(len(positions)):
        rnd = random.random()
        positions[i][1] = updatePosition(n, m, positions[i][1], rnd)


def sortPositions(positions):                               # mit key geordnet

    positions.sort(key=lambda x: x[1])                      # zweiter Eintrag


def extractSquare(positions):

    if len(positions) == 0:
        return []

    squarelist = []                                         # squarelist: list
    maxfigure = positions[len(positions)-1][1]              # maxfigure: int
    for i in range(len(positions)):
        if positions[i][1] == maxfigure:
            squarelist.append(positions[i])
            # Figuren auf dem Feld mit dem höchsten Index an square angehängt

    for i in range(len(squarelist)):
        positions.remove(squarelist[i])
        # square-Elemente aus positions entfernt

    return squarelist


def giftExchange(square):

    unpackedlist = [eintrag for figur in square for eintrag in figur]
    # unpackedlist: list; zwei for-Schleifen ineinander, zuerst figur in square
    # dann eintrag in figur, um nicht mehr Liste in Liste zu haben

    zombies = unpackedlist.count('Z')
    elfs = unpackedlist.count('ZH')
    humans = unpackedlist.count('H')
    harfs = unpackedlist.count('HH')
    # jeweils integers

    if elfs >= 1 and humans >= 1:                           # a)
        for i in range(len(square)):
            if square[i][0] == 'H':
                square[i][0] = 'HH'
                harfs += 1                                  # ints adjusted
                humans -= 1                                 # ints adjusted

    superhumans = humans + harfs

    if zombies >= 1 and superhumans >= 1:                   # b)
        if zombies >= 2*harfs:
            for i in range(len(square)):
                if square[i][0] == 'H' or square[i][0] == 'HH':
                    square[i][0] = 'Z'
        elif zombies < 2*harfs:
            for i in range(len(square)):
                if square[i][0] == 'Z':
                    square[i][0] = 'ZH'


def christmasFated(positions):

    unpackedlist = [eintrag for figur in positions for eintrag in figur]
    # siehe giftExchange

    if ('H' not in unpackedlist and 'HH' not in unpackedlist
            or 'Z' not in unpackedlist) and abfrage(unpackedlist):
        return True
    else:
        return False


def mergeSquare(square, intermediate):                      # zwei Listen als
    # Eingabe

    for lists in range(len(square)):
        if abfrage(square[lists]):
            intermediate.append(square[lists])


def christmasFate(positions):

    unpackedlist = [eintrag for figur in positions for eintrag in figur]

    if 'H' not in unpackedlist and 'HH' not in unpackedlist:
        returnstring = 'Zombies ate my Christmas!'
    elif 'Z' not in unpackedlist:
        returnstring = 'Ho, ho, ho, and a merry Zombie-Christmas!'

    return returnstring


def zombieChristmas(n, m, positions):

    intermediate = []

    while not christmasFated(positions):                    # while False
        updatePositions(n, m, positions)                    # Bewegung
        sortPositions(positions)                            # sortiert
        while abfrage(positions):
            square = extractSquare(positions)               # squares ermittelt
            giftExchange(square)                            # Geschenke und
            # Umwandlung der Figuren
            mergeSquare(square, intermediate)               # Sicherung der
            # Liste positions
        positions = intermediate
        intermediate = []

    return christmasFate(positions)


def abfrage(list1):
    if len(list1) == 0:
        return False
    else:
        return True
    # falls Inhalt nicht leer, True -> somit Abfrage einfacher
