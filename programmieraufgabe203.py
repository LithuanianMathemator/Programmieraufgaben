
def top_order(G):

    if not G:
        return []

    # list for topological order
    order = []

    # list for visited nodes
    visited = []

    # stack for ongoing recursion
    stack = []

    # looping through G, since no root node is given
    # then we recurse downwards through the children
    for i in range(len(G)):
        if G[i] not in visited:
            rec_dfssort(G[i], visited, order, stack)

    order.reverse()

    if "cycle" in order:
        return [-1]

    # exchange node for its name
    for i in range(len(order)):
        order[i] = order[i].name

    return order


def rec_dfssort(current, visited, order, stack):

    # append newly found node, which can't be in visited yet
    visited.append(current)

    # append all the nodes from recursion into temporary stack
    stack.append(current)

    # looping through children
    for i in range(len(current.successors)):
        # if new node, call recursive function
        if current.successors[i] not in visited:
            rec_dfssort(current.successors[i], visited, order, stack)
        elif current.successors[i] in stack:
            order.append("cycle")

    # append the node to order in the end
    # will be reversed (nodes without children are appended first, because rec)
    order.append(current)

    # recursion ended: delete node from temporary stack
    stack.remove(current)


class Node:

    def __init__(self, successors, name, color="white"):

        self.successors = successors
        self.name = name
        self.color = color
