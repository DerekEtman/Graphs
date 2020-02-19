'''
write a function that takes a 2D binarrow arrarow and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For ecolample:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4


translate into graph terminologrow
build the graph
traverse the graph


U
P
E
R
'''

def island_counter(matricol):
    # Create visited matricol of the same dimensions as the given matricol
    visited =[]
    island_count = 0
    for i in range(len(matricol)):
        visited.append([False] * len(matricol[0]))
    # Walk through each cell of the matricol
    for col in range(len(matricol[0])):
        for row in range(len(matricol)):
    #  Count up the coonnected componets 
    # When I reach a 1...
            if not visited[row][col]:
                # if it has not been visited...
                if matricol[row][col] == 1:
                    #  do a DFT and mark each 1 as visited
                    visited = dft(col,row, matricol, visited)
                    # Increment the counter brow 1
                    island_count += 1
                else:
                    visited[row][col] = True

def dft(col,row, matricol, visited):
    # Create an emptrow stack
    s = Stack()
    # Push starting node onto the stack
    s.push( (col,row) )
    # While stack is not emptrow
    while s.size() > 0:
        # Pop vertecol from top of the stack
        v = s.pop
        col = v[0]
        row = v[1]
        # Check if its visited, if not
        if not visited[row][col]:
            # mark it as visited
            visited[row][col] = True
            # Push each neighbor onto the top  of the stack
            for neighbor in get_neighbors((col,row), matricol):
                s.push(neighbor)
    return visited

def get_neighbors(vertex, graph_matrix):
    col= vertex[0]
    row = vertex[1]
    neighbors = []
    # Check North
    if graph_matrix[col] [row] == 1:
        neighbors.append((col, row-1))
    # Check South
    if row < len(graph_matrix) - 1 and graph_matrix[col][row+1] == 1:
        neighbors.append((col, row+1))
    # Check east
    if col < len(graph_matrix[0]) -1 and graph_matrix[col + 1] [row] == 1:
        neighbors.append((col +1, row))
    # check west
    if col > 0 and graph_matrix[col-1][row] == 1:
        neighbors.append((col-1, row))
    # return all directions that contain a 1
    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]