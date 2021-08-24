def linear_regression(points, lines):                   # Funktion definiert

    distancelist = []                                   # Liste definiert
    for i in range(0, len(lines)):                      # lines durchlaufen
        distancelist.append(get_linedistance(points, lines[i]))
        # n aus get_linedistance wird zu distancelist hinzugefügt
    return get_min(distancelist)                        # Minimum ausgegeben


def get_linedistance(points, line):                     # Funktion definiert

    pointlist = points                                  # Liste definiert
    linetuple = line                                    # Liste definiert
    n = 0                                               # Zählinteger
    for i in range(0, len(pointlist)):                  # points durchlaufen
        n += (linetuple[0]*pointlist[i][0]+linetuple[1]-pointlist[i][1])**2
        # n ist die Distanz
    return n                                            # n zurückgegeben


def get_min(int_list):                                  # Funktion definiert
    if len(int_list) == 0:                              # falls leer
        return None                                     # None wird returnt
    else:                                               # sonst
        return min(int_list)                            # Minimum returnt
