
def LU_decomposition(M):

    if M == '':
        return ''

    commalessM = M.replace(',', '')                         # removing commas

    mulM = commalessM.split()                               # numbers into list

    rowsM = M.count(',') + 1                                # matrice's rows

    for i in range(len(mulM)):                              # string to int

        if mulM[i][0] == '−':
            mulM[i] = int('-' + mulM[i][1:len(mulM[i])])
        else:
            mulM[i] = int(mulM[i], base=10)

    columnsM = int((len(mulM)/rowsM))                       # matrice's columns

    rowlist = [mulM[x:x+columnsM] for x in range(0, len(mulM), columnsM)]
    # list of A's rows

    if len(rowlist) == 1:
        return M

    lowerlist = []

    # Gauss elimination:

    for x in range(columnsM):
        # columns ->

        for i in range(1+x, rowsM):
            # downwards for each column

            subtractor = (rowlist[i][x]/rowlist[x][x])
            lowerlist.append([int(subtractor), i, x])

            for j in range(x, columnsM):
                # columns x->

                rowlist[i][j] = int((rowlist[i][j] -
                                     (subtractor*rowlist[x][j])))

    for i in range(len(lowerlist)):
        rowlist[lowerlist[i][1]][lowerlist[i][2]] = lowerlist[i][0]
        # exchanging zeros for numbers of U

    rowlist = [number for numberlist in rowlist for number in numberlist]
    # unpacking rowlist: for list in rowlist: \ for number in list

    for i in range(len(rowlist)):
        rowlist[i] = str(rowlist[i])
        # ints become strings

    for i in range(len(rowlist)-1):
        if (i+1) % columnsM == 0:
            rowlist[i] += ','
            # commas behind ends of row without last row

    for i in range(len(rowlist)-1):
        rowlist[i] += ' '
        # spaces behind each number in C except for last one

    LUmatrice = ''.join(rowlist)
    # list to string

    return LUmatrice
