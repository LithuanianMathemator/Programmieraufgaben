from math import sqrt


def sieve(n):                                           # Funktion definiert

    sievelist = []                                      # füllbare, neue Liste

    if n < 2:                                           # bei n < 2
        return None                                     # return None
    else:
        for sieb in range(2, n+1):                      # für n größer 1
            for teiler in range(2, int(sqrt(sieb))+1):  # 2 bis Wurzel der Zahl
                if sieb % teiler == 0:                  # teilbar durch teiler?
                    break                               # if not prime: break
            else:                                       # no-break-else für for
                sievelist.append(sieb)                  # n zu Liste, wenn prim
        return sievelist                                # return von Liste


def isprime(n):                                         # Funktion definiert

    if n < 2:                                           # bei n < 2
        return None                                     # return None
    else:
        for teiler in range(2, int(sqrt(n))+1):         # teiler: 2 to wurzel n
            if n % teiler == 0:                         # falls teilbar
                return False                            # False
                break                                   # for wird abgebrochen
        else:
            return True                                 # sonst Primzahl


def exponents(a, b):                                    # Funktion für Faktoren
    counter = 0                                         # while counter
    while a % b == 0:                                   # wenn restlos teilbar
        a = a/b                                         # Zahl nun Quotient
        counter += 1                                    # Exponent errechnet
    return [b, counter]                                 # Liste zurückgegeben


def factorization(n):                                   # Funktion definiert

    factorlist = []
    # leere Liste
    # zum gefüllt werden
    m = int(n/2)+1
    # wie in Beschreibung der Aufgabe m definiert

    if n < 2:                                           # falls n < 2
        return None                                     # return  None
    elif isprime(n):                                    # falls prim
        factorlist.append([n, 1])                       # nur sie selbst hoch 1
    else:                                               # andernfalls
        for prime in sieve(m):
            # sieve Elemente werden als Teiler im folgenden durchlaufen
            if n % prime == 0:                          # wenn teilbar
                factorlist.append(exponents(n, prime))
                # Liste erweitert
                # um exponents return

    return factorlist                                   # Liste returned


def divisornumber(n):                                   # Funktion definiert

    elist = factorization(n)
    # elist ist nun unsere Liste der Primzahlzerlegung
    tau = 1
    # integer für spätere Multiplikation der Exponenten

    if n < 1:                                           # falls n kleiner 1
        return None                                     # return None
    elif n == 1:                                        # n ist Eins
        return 1                                        # also wird 1 returned
    else:                                               # andernfalls
        amount = len(elist)
        # Menge der Elemente der Liste
        for i in range(0, amount):                      # für Elemente der list
            tau *= (elist[i][1]+1)
            # in der for-Schleife werden die jeweils zweiten Werte der Listen
            # in der Liste um Eins erhöht und dann nacheinander anhand deren
            # Stelle i in der Liste miteinander multipliziert

        return tau


def iscoprime(n, m):                                    # Funktion definiert

    if n < 1 or m < 1:                                  # falls n oder m < 1
        return None                                     # return None
    else:
        return divisornumber(n*m) == divisornumber(n)*divisornumber(m)
    # falls die Gleichung (2) aus der Aufgabenstellung gilt, sind n und m
    # teilerfremd und True wird zurückgegeben
    # ist weder n noch m kleiner 1 und sind die beiden Zahlen nicht teilerfremd
    # so wird False zurückgegeben
