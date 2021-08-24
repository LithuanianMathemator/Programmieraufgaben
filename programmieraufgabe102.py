
def get_lattice_point_number(h, a1, a2, b1, b2):    # Definition der Funktion

    if h < 0:
        return "Die Eingabe ist fehlerhaft."

    def convert_to_standard(a1, a2, b1, b2):        # Definition Konvertierung
        b2, a2 = max(a2, b2), min(a2, b2)
    # a2 größer b2 bedeutet
    # vertauschte Ecken
    # also werden
    # a2 und b2 vertauscht

        return a1, a2, b1, b2                        # neue Ecken zurückgegeben

    a1, a2, b1, b2 = convert_to_standard(a1, a2, b1, b2)

    def intersects(h, a1, a2, b1, b2):               # haben Rechtecke Schnitt?
        if b1 < 0 or b2 < 0:                         # Rechteck zu weit links
            return False                             # oder unten
        elif a1 > 6:                                 # Rechteck rechts daneben
            return False
        elif a2 > h:                                 # Rechteck obendrüber
            return False
        else:
            return True

    if intersects(h, a1, a2, b1, b2):                   # falls Schnitt
        def get_delta_x1(a1, b1):
            if b1 > 6 and a1 >= 0:                      # |a|b
                x1 = 6-a1
            elif b1 <= 6 and a1 >= 0:                   # |ab|
                x1 = b1-a1
            elif b1 <= 6 and a1 < 0:                    # a|b|
                x1 = b1
            elif b1 > 6 and a1 < 0:                     # a||b
                x1 = 6
            return x1

    if intersects(h, a1, a2, b1, b2):
        def get_delta_x2(h, a2, b2):
            if b2 > h and a2 >= 0:                      # |a|b
                x2 = h-a2
            elif b2 <= h and a2 >= 0:                   # |ab|
                x2 = b2-a2
            elif b2 <= h and a2 < 0:                    # a|b|
                x2 = b2
            elif b2 > h and a2 < 0:                     # a||b
                x2 = h
            return x2

    if intersects(h, a1, a2, b1, b2):               # nur bei Schnitt gibt es L
        L = (get_delta_x1(a1, b1)+1)*(get_delta_x2(h, a2, b2)+1)
    # L benötigt +1 bei x1
    # und x2, da Fläche nicht gleich Punkte,
    # dann wird das Rechteck berechnet

    if intersects(h, a1, a2, b1, b2):               # bei Schnitt Punkte
        return "Die Zahl der Gitterpunkte im resultierenden \
Rechteck betraegt " + str(L) + "."
    else:                                               # sonst leer
        return "Der Schnitt der gegebenen Rechtecke ist leer."
