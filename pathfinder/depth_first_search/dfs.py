graph = \
    {
        0: [1,2],
        1: [0,2],
        2: [3,4],
        4: [0],
        5: [],
        3: [5,4]
    }

graph1 = \
    {
        0: [1,2],
        1: [2],
        2: [0,3],
        3: [3]
    }

def dfs(graph, start):
    '''
    keep visiting neighbors till there are no more left
    then back track to the most recently added node
    which have not been explored.
    '''
    
    visited = []
    path = []
    yet_to_explore = []
    total_nodes = len(graph.keys())

    while True:##before 4 can be added . len it exceeded
        
        neighbors = graph.get(start)

        visited.append(start) if start not in visited else None
        path.append(start) if start not in path else None
        
        if len(path)==total_nodes:
            break
        if len(neighbors)== 0:
            # this is where we backtrack
            # all the visited once till we 
            # find a node whose neighbors are not all exhausted

            #all neighbors are visited, so start is totally explored
            # path.append(start)
            
            for i in visited[::-1]:
                if i not in path:
                    start = i
                    break

        else:
            
            count = 0
            for neighbor in neighbors:
                
                if neighbor not in visited:
                    # visited.append(neighbor)
                    # path.append(start) if start not in path else None
                    start = neighbor
                    count += 1
                    break
                    
            ## all neighbors for this start is already visited.
            ## we need to back track from this path. else it is
            ## causing a cycle
            if count == 0:
                path = [i for i in visited if i!=start]
                start = path[-1]

    print(path,visited)


def dfs1(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
        remove_from_stack = True
        for next in graph.get(node):
            if next not in visited:
                stack.append(next)
                remove_from_stack = False
                break
            if remove_from_stack:
                stack.pop()
    return visited

def execute():
    start = 0
    dfs1(graph, start)

execute()