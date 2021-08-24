
def multiply(A, B):

    if A == '' or B == '':
        return ''

    commalessa = A.replace(',', '')                         # removing commas
    commalessb = B.replace(',', '')

    mula = commalessa.split()                               # numbers into list
    mulb = commalessb.split()

    rowsa = A.count(',') + 1                                # matrice's rows
    rowsb = B.count(',') + 1

    for i in range(len(mula)):                              # string to int
        mula[i] = int(mula[i], base=10)
    for i in range(len(mulb)):
        mulb[i] = int(mulb[i], base=10)

    columnsa = int((len(mula)/rowsa))                       # matrice's columns
    columnsb = int((len(mulb)/rowsb))

    rowlist = [mula[x:x+columnsa] for x in range(0, len(mula), columnsa)]
    # list of A's rows
    columnlist = [mulb[x::columnsb] for x in range(0, columnsb)]
    # list of B's columns

    clist = []

    for i in range(len(rowlist)):
        for j in range(len(columnlist)):
            clist.append(matmul(rowlist[i], columnlist[j]))
            # list like mul for C

    rowsc = rowsa
    columnsc = columnsb
    # rows and columns of c

    for i in range(len(clist)):
        clist[i] = str(clist[i])
        # ints become strings

    for i in range(len(clist)-1):
        if (i+1) % columnsc == 0:
            clist[i] += ','
            # commas behind ends of row without last row

    for i in range(len(clist)-1):
        clist[i] += ' '
        # spaces behind each number in C except for last one

    newmatrice = ''.join(clist)
    # list to string

    return newmatrice


def power(A, m):

    newA = A                                                # saving initial A
    for i in range(1, m):                                   # muliply m times
        A = multiply(A, newA)
        # A becomes product of A^i and A

    return A


def matmul(list1, list2):

    alllist = []

    for i in range(len(list1)):
        alllist.append(list1[i]+list2[i])

    return min(alllist)
