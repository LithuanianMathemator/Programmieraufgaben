
class Node:

    def __init__(self, key, leftChild, rightChild, parent, bal=None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
        self.bal = bal

    def balance(self):
        # children must exist
        if self.leftChild or self.rightChild:
            # recursive call for left part-tree
            if self.leftChild:
                highleft = self.leftChild.balance()
            else:
                # if no child, other one definitely longer
                highleft = 0
            # recursive call for right part-tree
            if self.rightChild:
                highright = self.rightChild.balance()
            else:
                # if no child, other one definitely longer
                highright = 0

            self.bal = highright-highleft
            return max(highleft, highright) + 1
        else:
            return 0


class AVLTree:

    def __init__(self, root):
        self.root = Node(root, None, None, None)

    def insert(self, key):
        # first insert new node
        z = Node(key, None, None, None)
        y = None
        x = self.root

        while x != None:
            y = x
            if z.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild

        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # now check for imbalances, repair if needed
        p = z.parent
        while p != None:
            p.balance()
            if p.bal == -2 and (p.left.bal == 0 or p.left.bal == -1):
                rotateright(p)
            elif p.bal == -2 and p.left.bal == 1:
                rotateLR(p)
            elif p.bal == 2 and (p.left.bal == 0 or p.left.bal == -1):
                rotateleft(p)
            else:
                rotateRL(p)

            p = p.parent

    def rotateright(self, x):

        y = x.leftChild

        # change parents child
        if x.parent == None:
            self.root = y
        elif x.parent.leftChild == x:
            x.parent.leftChild = y
        else:
            x.parent.right = y

        # change y parent
        y.parent = x.parent
        # shift child of y to x
        x.leftChild = y.rightChild

        # new parent for former child of y
        if x.leftChild != None:
            x.leftChild.parent = x

        # new child of y is x
        y.rightChild = x
        # change parent of x
        x.parent = y

    def rotateleft(self, x):

        y = x.rightChild

        # change parents child
        if x.parent == None:
            self.root = y
        elif x.parent.leftChild == x:
            x.parent.leftChild = y
        else:
            x.parent.right = y

        # change y parent
        y.parent = x.parent
        # shift child of y to x
        x.rightChild = y.leftChild

        # new parent for former child of y
        if x.rightChild != None:
            x.rightChild.parent = x

        # new child of y is x
        y.leftChild = x
        # change parent of x
        x.parent = y

    def rotateLR(self, x):
        rotateleft(x.leftChild)
        rotateright(x)

    def rotateRL(self, x):
        rotateright(x.rightChild)
        rotateleft(x)
