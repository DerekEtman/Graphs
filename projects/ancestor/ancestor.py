# Problem: Find the earliest ancestor from the input individual, if there are multiples return the lowest number between them
# Graph Solving Framework:
# 1. Translate into graph terminology
    # Undirected Graph
    # 
# 2. Build your graph
# 3. Traverse the graph
# Undirected 



class Node():
    def __init__(self, value, distance):
        self.value = value
        self.distance = distance

def earliest_ancestor(ancestors, starting_node):
    # Create empty path array
    path = []
    # Create starting Node
    start = Node(starting_node, 0)
    # Create a queue for storing path
    q = []
    # Begin with starting node
    q.append(start)
    path.append(start)
    # Search Loop:
    while len(q) > 0:
        # Pop the top of the stack
        node = q.pop(0)
        #print(node.value)
        # Loop through the graph
        for pair in ancestors:
            # Check to see if it has a parent
            if node.value == pair[1]:
                # create new node with that value
                new_node = Node(value=pair[0],
                                distance=node.distance + 1)
                # Push to Stack
                q.append(new_node)
                path.append(new_node)
    if len(path) == 1:
        return -1
    elif path[-1].distance == path[-2].distance:
        if path[-1].value > path[-2].value:
            return path[-2].value 
        else:
            return path[-1].value
    else:
        return path[-1].value
        