
def maxunimod(L):

    if len(L) == 1:
        return 1
        # just one element: just one sequence with length 1

    counter = 0
    # for index of list

    length = 1

    lenlist = []
    # list for lengths of sequences

    if L[0] <= L[1]:
        direction = 1
        # 1: upwards

    if L[0] > L[1]:
        direction = -1
        # -1: downwards

    while counter < len(L)-1:

        if direction == 1:
            if L[counter] <= L[counter+1]:
                length += 1
                counter += 1
            else:
                direction = -1
                # direction switches

        if direction == -1:
            if L[counter] >= L[counter+1]:
                length += 1
                counter += 1
            else:
                # end of sequence
                lenlist.append(length)
                length = 1
                direction = 1
                while L[counter] == L[counter-1]:
                    counter -= 1
                    # if last elements of sequence were equal, go to the first

    lenlist.append(length)
    # append last length

    return max(lenlist)
    # return maximum length
