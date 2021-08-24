
def abstand(s, t, dateiname="labyrinth.dat"):

    labfile = dateiname

    strecke = 0
    # integer for distance
    rowlists = []
    # list to fill

    with open(labfile, 'r') as file:
        for line in file:
            rowlists.append([letter for letter in line])
            # opens file and puts each rows elements
            # into separate lists in list

    if rowlists == []:
        return -1

    letterindex = len(rowlists[0])-1
    # integer for index of '\n'

    for row in range(len(rowlists)):
        rowlists[row].remove(rowlists[row][letterindex])
        # '\n' removed from each row'

    startindex = s[0]*(len(rowlists[0]))+s[1]+1
    # integer
    targetindex = t[0]*(len(rowlists[0]))+t[1]+1
    # integer

    spalten = len(rowlists[0])

    for row in range(len(rowlists)):

        for letter in range(spalten):
            if rowlists[row][letter] == 'P':
                rowlists[row][letter] = row*(len(rowlists[0]))+letter+1

            # exchanges P with number of knot

    if s[0] >= len(rowlists) or s[1] > spalten or \
            t[0] >= len(rowlists) or t[1] > spalten:
        return -1
        # input bigger than allowed

    if s[0] < 0 or s[1] < 0 or \
            t[0] < 0 or t[1] < 0:
        return -1
        # input lower than allowed

    # print(rowlists)

    unpackedlist = [field for row in rowlists for field in row]
    # list with U's and the numbered fields

    if targetindex not in unpackedlist:
        return -1
        # targetindex is 'U'

    if startindex not in unpackedlist:
        return -1
        # startindex is 'U'

    if startindex == targetindex:
        return 0
        # no move has to be made

    # BFS in the following:

    traveledcounter = 0
    traveled = [startindex]
    # traveled knots go in here
    queue = [[startindex, s[0], 0]]
    # queue FIFO with the row in rowlists of the element
    lenrow = len(rowlists[0])

    while abfrage(queue):
        # while there are testable objects

        if (queue[0][0]+1) in unpackedlist:
            # element must exist and be int, not 'U'
            if (queue[0][0]+1) in rowlists[queue[0][1]]:
                # has to be in same row
                if [(queue[0][0]+1), queue[0][1], queue[0][2]+1] not in queue \
                        and (queue[0][0]+1) not in traveled:
                    queue.append([(queue[0][0]+1), queue[0][1], queue[0][2]+1])
                    # if not in queue and not in traveled, append
                if (queue[0][0]+1) not in traveled:
                    traveled.append((queue[0][0]+1))
                    # if not in traveled, append
                    # if on the right of queue[0][0] is 'P'

        if (queue[0][0]-1) in unpackedlist:
            # element must exist and be int, not 'U'
            if (queue[0][0]-1) in rowlists[queue[0][1]]:
                # has to be in the same row
                if [(queue[0][0]-1), queue[0][1], queue[0][2]+1] not in queue \
                        and (queue[0][0]-1) not in traveled:
                    queue.append([(queue[0][0]-1), queue[0][1], queue[0][2]+1])
                    # if not in queue and not in traveled, append
                if (queue[0][0]-1) not in traveled:
                    traveled.append((queue[0][0]-1))
                    # if not in traveled, append
                    # if on the left of queue[0][0] is 'P'

        if (queue[0][0]+lenrow) in unpackedlist and (queue[0][0]+lenrow) \
                not in traveled:
            # element must exist and be int, not 'U'
            if [(queue[0][0]+lenrow), queue[0][1]+1, queue[0][2]+1] \
                    not in queue and (queue[0][0]+lenrow) not in traveled:
                queue.append([(queue[0][0]+lenrow),
                              queue[0][1]+1, queue[0][2]+1])
                # if not in queue and not in traveled, append
            if (queue[0][0]+lenrow) not in traveled:
                traveled.append((queue[0][0]+lenrow))
                # if not in traveled, append
                # if on the top of queue[0][0] is 'P'

        if (queue[0][0]-lenrow) in unpackedlist and (queue[0][0]-lenrow) \
                not in traveled:
            # element must exist and be int, not 'U'
            if [(queue[0][0]-lenrow), queue[0][1]-1, queue[0][2]+1] \
                    not in queue and [(queue[0][0]-lenrow), queue[0][1]-1,
                                      queue[0][2]+1] not in traveled:
                queue.append([(queue[0][0]-lenrow),
                              queue[0][1]-1, queue[0][2]+1])
                # if not in queue and not in traveled, append
            if (queue[0][0]-lenrow) not in traveled:
                traveled.append((queue[0][0]-lenrow))
                # if not in traveled, append
                # if on the bottom of queue[0][0] is 'P'

        if queue[0][0] == targetindex:
            return queue[0][2]
            break
            # if target found, return disctance traveled

        queue.pop(0)
        # if top left bottom right tested, pop first element

    return -1
    # if while does not break and return distance, start and target in
    # different partitions


def abfrage(list1):
    if len(list1) == 0:
        return False
    else:
        return True
    # falls Inhalt nicht leer, True -> somit Abfrage einfacher
