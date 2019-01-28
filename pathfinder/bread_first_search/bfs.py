# from collections import defaultdict

# graph = [(0, [1,2]), (1,[0,2]),(2,[3,4]),(3,[4,5]),(4,[0])]

# d = {}
# for k,v in graph:

#     d.setdefault(k,[]).append(v)
#     print(k,v)

# print(d)

graph = \
    {
        0: [1,2],
        1: [0,2],
        2: [3,4],
        4: [0],
        5: [],
        3: [4,5]
    }


graph1 = \
    {
        0: [1,2],
        1: [2],
        2: [0,3],
        3: [3]
    }

def bfs(graph, start):

    visited = []

    explored = []

    total_number_of_nodes = len(graph.keys())
    
    while len(visited) < total_number_of_nodes:

        neighbors = graph.get(start)
        visited.append(start) if start not in visited else None
        
        if neighbors:

            first_neighbor = neighbors[0]
            neighbor_visits= []

            [neighbor_visits.append(x) if x not in visited else None for x in neighbors]
            
            if len(neighbor_visits) == 0:
                ## we have already visited those places, so start is already explored
                ## so we will now start by exploring the last not explored place
                explored.append(start)
                start = visited[-1]
                
            else:             
            ## we have visited all the neighbors and now we would explore the
            ## very first visited neighbor.
            ## the way we would do this is we would set start = first neighbor
                visited.extend(neighbor_visits)
                explored.append(start)
                start = first_neighbor
                

        else:
            ## there are no neighbors, we can simply mark start as explored
            ## and our next node for exploration would be last visited one
            explored.append(start)
            start = visited[-1]

    print(explored, visited)

def execute():
    
    start = 2
    bfs(graph1, start)
    
execute()
