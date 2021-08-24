
# 1. Aufgabe


def monoton(L):

    # trivial case:
    if len(L) == 1:
        return 1

    counter = 0

    # 1 for upwards, -1 for downwards
    direction = 0

    length = 1

    lenlist = []

    # determine which direction to begin with
    if L[0] <= L[1]:
        direction = 1

    if L[0] > L[1]:
        direction = -1

    while counter < len(L)-1:
        if direction == 1:
            if L[counter] <= L[counter+1]:
                length += 1
                counter += 1
            else:
                lenlist.append(length)
                length = 1
                direction = -1
                while L[counter] == L[counter-1]:
                    counter -= 1

        if direction == -1:
            if L[counter] >= L[counter+1]:
                length += 1
                counter += 1
            else:
                lenlist.append(length)
                length = 1
                direction = 1
                while L[counter] == L[counter-1]:
                    counter -= 1

            # go forwards, test direction, at change stop for one iteration,
            # update values and append the counted length
            # if last elements of previous sequence were equal, go backwards
            # until firsz element of constant sequence is found

    # append last length
    lenlist.append(length)

    return max(lenlist)


# 2. Aufgabe

# (a)

def is_Intlist_Palindrom(C):

    # trivial case:
    if len(C) == 0:
        return True

    # lists to later compare
    fromleft = []
    fromright = []

    if len(C) % 2 == 0:

        for i in range(0, len(C)//2):
            fromleft.append(C[i])

        for i in range(len(C)-1, len(C)//2-1, -1):
            fromright.append(C[i])

    else:

        for i in range(0, len(C)//2+1):
            fromleft.append(C[i])

        for i in range(len(C)-1, len(C)//2-1, -1):
            fromright.append(C[i])

            # test list depending on whether or not lenght is even

    if fromleft == fromright:
        return True
    else:
        return False
        # compare lists, return corresponding value

# (b)


def is_Int_Palindrom(c):

    # handle case in which c is smaller than zero
    if c < 0:
        return None

    intlist = [int(ziffer) for ziffer in str(c)]
    # take number as string and append int() of letters to list
    # then use function from part (a)

    return is_Intlist_Palindrom(intlist)


# 3. Aufgabe

def is_Tree(G):

    n = 0
    # counter for edges

    for i in range(len(G)):
        n += len(G[i])

    n = n//2

    # amount of edges for tree
    if n != len(G)-1:
        return False

    if len(G) == 1:
        return True
        # one node -> tree
    elif [] in G:
        return False
        # graph not connected
    else:
        return True
        # connected and n-1 edges -> tree


# 4. Aufgabe

def add_Normalized(A, B):

    R = []

    # reassigning list variables so lists do not get altered -> easier testing
    X = []
    Y = []
    for i in range(6):
        X.append(A[i])
        Y.append(B[i])

    uebertrag = 0

    # one number = zero: (this part is basically useless, the rest works
    # equally well without handling the case in advance)
    if X == [0, 0, 0, 0, 0, 0]:
        return Y

    if Y == [0, 0, 0, 0, 0, 0]:
        return X

    if X[5] < Y[5]:
        X, Y = Y, X

    n = X[5] - Y[5]

    if n > 4:
        return X
        # number B too small
    elif n > 0 and n < 5:
        for i in range(4, -1, -1):
            if i - n >= 0:
                Y[i] = Y[i-n]
            else:
                Y[i] = 0
                # adjust smaller number to bigger exponent

    for i in range(4, -1, -1):

        x = X[i] + Y[i] + uebertrag

        if x > 8:
            uebertrag = 1
            R.insert(0, x % 9)
        else:
            uebertrag = 0
            R.insert(0, x % 9)
            # written addition

    if uebertrag == 1:
        R.pop()
        R.insert(0, 1)
        R.append(X[5] + 1)
        # adjust number by cutting last digit, adding one at the beginning
        # and raising exponent
    else:
        R.append(X[5])
        # otherwise adding the exponent is enough

    return R
