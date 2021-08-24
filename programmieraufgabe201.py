
class Node:
    def __init__(self, key, leftChild, rightChild):
        # left for leftChild, right for rightChild
        self.leftChild = leftChild
        self.rightChild = rightChild
        # data shall be key
        self.key = key

    def keys(self):
        keylist = []
        # append root
        keylist.append(self.key)
        # if not None
        if self.leftChild:
            keylist += self.leftChild.keys()
        # if not None
        if self.rightChild:
            keylist += self.rightChild.keys()
        # += to fuze the resulting lists
        return keylist

    def height(self):
        # children must exist
        if self.leftChild or self.rightChild:
            # recursive call for left part-tree
            if self.leftChild:
                highleft = self.leftChild.height()
            else:
                # if no child, other one definitely longer
                highleft = 0
            # recursive call for right part-tree
            if self.rightChild:
                highright = self.rightChild.height()
            else:
                # if no child, other one definitely longer
                highright = 0
            return max(highleft, highright) + 1
        else:
            return 0

    def leaves(self):
        leaveslist = []
        # if children
        if self.leftChild or self.rightChild:
            # if not None
            if self.leftChild:
                leaveslist += self.leftChild.leaves()
            # if not None
            if self.rightChild:
                leaveslist += self.rightChild.leaves()
        else:
            # append if no children
            leaveslist += [self.key]

        return leaveslist
