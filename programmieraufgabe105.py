
def get_eqclasses(n, E):
    eqlist = get_classes(n, E)                          # Liste aus get_classes
    # wird eqlist zugewiesen
    removelist = []
    list1 = []
    for i in range(n):                                  # für die Knoten in n
        for j in range(i+1, n):                         # der Knoten nach #
            # für jeden Knoten in n werden die nachfolgenden Knoten geprüft
            # darauf,
            # ob entweder die Mengen disjunkt sind, z.B. [0] und [1,2], oder
            # aber, ob die Mengen gleich sind, z.B. [3,1,2] und [1,2,3]
            # dies wird mithilfe are_disjoint oder are_equal gemacht und prüft
            # so die Bedingung für eine Äquivalenzklasse aus dem Lemma
            if not are_disjoint(eqlist[i], eqlist[j]) \
                    and not are_equal(eqlist[i], eqlist[j]):
                return []
                # ist keine der beiden Bedingungen für eine Menge aus eqlist
                # erfüllt, so weiß man aus dem Lemma, dass die Relation auf V
                # keine Äquivalenzrelation ist

            # ist die Relation eine Äquivalenzrelation, so werden im
            # folgenden
            # noch die induzierten, zugrundeliegenden Partitionen ermittelt

            if are_equal(eqlist[i], eqlist[j]):
                removelist.append(eqlist[j])
                # falls die Mengen äquivalent sind, wird der removelist das
                # doppelte Element beigefügt
                # dieses kann dann später aus der eqlist entfernt werden, die
                # im Grunde genommen bereits alle Elemente enthält, die in der
                # Ausgabe erwünscht sind

    for i in range(len(removelist)):                    # für die Länge der
        # Liste
        if removelist[i] not in list1:                  # falls noch nicht drin
            list1.append(removelist[i])                 # hinzugefügt
            # hier soll Doppelung unter den Elementen in der removelist
            # verhindert werden, da sonst nicht sauber von der eqlist abgezogen
            # werden kann
            # dafür wird einer zunächst leeren Liste immer dann etwas
            # hinzugefügt, wenn das Element noch nicht enthalten ist, so dass
            # keine Elemente zweimal hinzugefügt werden können

    for i in range(len(list1)):
        eqlist.remove(list1[i])
        # jetzt werden einfach der Reihe nach die von den beinhalteten
        # Elementen (Zahlen) her doppelten Elemente (Listen) von der eqlist
        # abgezogen und es bleiben die Partitonen übrig
        # die Ermittlung doppelter Elemente geht hier auf Zeile 25 zurück

    return eqlist


def get_classes(n, E):                                  # Funktion definiert
    classlist = [[knot] for knot in range(n)]           # eine Liste für jeden
    # Knoten, der durch n gefordert wird, damit später zu den "Minilisten"
    # die jeweiligen Nachbarn hinzugefügt werden können
    for kantentupel in E:                               # für die Kantentupel
        # in E
        classlist[kantentupel[0]].append(kantentupel[1])  # wenn erster Knoten
        # aus Kantentupeln mit Knoten aus den "Minilisten" [knot] übereinstimmt
        # wird zweiter Knoten in die "Miniliste" als Nachbar hinzugefügt
        # nur in eine Richtung, da der Graph gerichtet ist, also Digraph
        # Anmerkung: basically das Codesnippet aus dem Lemma, hoffe mal das ist
        # erlaubt

    return classlist


def are_equal(list1, list2):                            # Funktion definiert
    setequal1 = set(list1)                              # Liste als Set
    setequal2 = set(list2)                              # Liste als Set
    if setequal1 == setequal2:                          # übereinstimmen Mengen
        return True                                     # return True
    else:                                               # sonst
        return False                                    # return False


def are_disjoint(list1, list2):                         # Funktion definiert
    setdis1 = set(list1)                                # Liste als Set
    setdis2 = set(list2)                                # Liste als Set
    if setdis1.isdisjoint(setdis2):                     # falls disjunkt
        return True                                     # return True
    else:                                               # nicht disjunkt
        return False                                    # return False
