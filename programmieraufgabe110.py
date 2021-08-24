
# import random

def quicksort(list, pivotFunction, lo=0, hi=-2):

    if hi == -2:
        hi = len(list)
        # hi initialisieren, falls erster Aufruf, sonst nie -2
    else:
        pass

    if lo < hi:
        # solange zu partitionierender Bereich 2 oder mehr Elemente hat

        pivot = pivotFunction(list, lo, hi-1)
        # Pivotelement bestimmen
        partition(list, lo, hi-1, pivotFunction)
        # um Pivotelement partitionieren
        pivotindex = list.index(pivot)
        # Index des nun sortierten Pivotelementes

        quicksort(list, pivotFunction, lo, pivotindex)
        quicksort(list, pivotFunction, pivotindex+1, hi)
        # rekursiver Aufruf für Elemente kleiner als Pivotelement und für
        # Elemente größer als Pivotelement


def indiepartition(list, lo, hi, pivotFunction):

    pivot = pivotFunction(list, lo, hi)
    # Pivotelement, um welches die Liste partitioniert wird
    pivotindex = list.index(pivot)
    # Index des Pivotelements

    floater = lo-1
    # stoppt nur, wenn Element größer als das Pivotelement ist, um die
    # Elemente, die größer als pivot sind, nach hinten zu befördern

    for i in range(lo, hi):

        if list[i] <= pivot:
            floater += 1
            list[i], list[floater] = list[floater], list[i]

        else:
            pass

    list[floater], list[pivotindex] = list[pivotindex], list[floater]
    # Pivotelement und aktuelles "Floaterelement" getauscht, damit
    # Pivotelement an richtiger Stelle

    # return list


def pivotFunction(list, lo, hi):
    randlist = list[lo:hi]
    # print(random.choice(randlist))
    return list[lo]


# def alternativepartition(list, lo, hi, pivotFunction):
#
#     i = lo
#     j = hi
#     pivot = pivotFunction(list, lo, hi)
#
#     while i < j:
#
#         while list[i] <= pivot:
#             i += 1
#
#         while list[j] > pivot:
#             j -= 1
#
#         if i < j:
#             list[i], list[j] = list[j], list[i]
#
#     pivotindex = list.index(pivot)
#
#     list[pivotindex], list[j] = list[j], list[pivotindex]
#
#     return list


def partition(list, lo, hi, pivotFunction):

    pivot = pivotFunction(list, lo, hi)
    # Pivotelement bestimmt

    if lo < hi:

        lowlist = []
        # Liste für kleinere Elemente
        highlist = []
        # Liste für größere Elemente

        for i in range(lo, hi+1):

            if list[i] < pivot:
                lowlist.append(list[i])
                # kleinere Elemente in lowlist
            elif list[i] > pivot:
                highlist.append(list[i])
                # größere Elemente in highlist
            else:
                pass
                # bei Pivotelement nichts

        exchangelist = lowlist + [pivot] + highlist
        # Partitionierung als Liste

        for i in range(lo, hi+1):
            list[i] = exchangelist[i-lo]
            # Teil der Liste ausgetauscht
