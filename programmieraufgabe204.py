
class Set:

    def __init__(self, V):

        # initialize attribute
        self._elements = V

    def Elements(self):

        # first sort for x[0], then x[1]
        self._elements.sort(key=lambda x: [x[0], x[1]])

        return self._elements


class Partition:

    def __init__(self, V):

        self.Sets = []

        # doubles if set is smaller
        if len(V) != len(set(V)):
            raise Exception("invalid operation")

        for i in range(len(V)):

            # Set in one list each
            self.Sets.append(Set([V[i]]))

    def __str__(self):

        return str([self.Sets[i]._elements for i in range(len(self.Sets))])

    def MakeSet(self, x):

        # if x already there, exception
        for i in range(len(self.Sets)):
            if x in self.Sets[i]._elements:
                raise Exception("invalid operation")

        self.Sets.append(Set([x]))

    def FindSet(self, x):

        # return first element of list that contains x
        for i in range(len(self.Sets)):
            if x in self.Sets[i]._elements:
                return self.Sets[i]._elements[0]

        # if no return happened, exception
        raise Exception("invalid operation")

    def Union(self, x, y):

        unionlist = []

        # find x
        for i in range(len(self.Sets)):
            if x == self.Sets[i]._elements[0]:
                unionlist.append(self.Sets[i])

        # find y
        for i in range(len(self.Sets)):
            if y == self.Sets[i]._elements[0]:
                unionlist.append(self.Sets[i])

        # if one was not found, exception
        if len(unionlist) != 2:
            raise Exception("invalid operation")

        # remove Set x and Set y from Sets
        for i in range(len(unionlist)):
            self.Sets.remove(unionlist[i])

        # join both lists in new one
        newunion = unionlist[0]._elements

        newunion += unionlist[1]._elements

        # make new Set xy
        newset = Set(newunion)

        # append lexicographically sorted Set xy to Sets
        self.Sets.append(Set(newset.Elements()))
