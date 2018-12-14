'''
We are going to create a grid square .

We will ask our a* algorithm to find the shortest distance
between top most left node to bottom most right node

Once found, we will also perform some optimization techniques
such as changing the neighbor values and changing the distance
metric

Assumptions:
<i> We know the start node, and the end node</i>
<i> We do not know the neighbors of a particular node.</i>

'''
import numpy as np 
from matplotlib import pyplot as plot 
from math import sqrt
from copy import deepcopy

class Location(object):

    def __init__(self, x , y):

        ##total cost at this node
        self.f_cost = 0

        ## cost of arriving at this particular node
        self.g_cost = 0

        ## heuristic/guess of cost of travelling from this node to end node
        self.h_cost = None

        ## neighbor will be filled in later
        ## essentially it is going to be  a list of Location objects
        self.neighbor = []


        ## x.y co-ordinates of this particular  node
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ':'+ str(self.y)

def calculate_distance(a, b):
    # a = np.array((a.x,a.y))
    # b = np.array((b.x, b.y))
    
    return round(sqrt(  (a.x - b.x)**2 + (a.y - b.y)**2  ))

def display_map(location_list, start_node, end_node):
    
    plot.scatter([i.x for i in location_list], [i.y for i in location_list], marker ='x')
    plot.scatter(start_node.x,start_node.y,facecolors='red',alpha=.55, s=100, label = 'start')
    plot.scatter(end_node.x,end_node.y,facecolors='green',alpha=.55, s=100, label = 'end')
    plot.title("Cities to Hit")
    plot.legend(loc='best')
    plot.show()



## we will take an optimization parameter here. since our data doesnt describe how to get the neighbors
## we will take a distance measure say 500. 
## our goal will to find neighbors where the distance betwen them is less than or equal to distance measure given
def find_neighbors(location, location_list, neighbor_distance = 500):

    neighbors = list(filter(\
            lambda i : 0 < calculate_distance(i,location) <= neighbor_distance,
                    location_list))


    return neighbors


def find_shortest_route(start_node, end_node):

    open_set = [start_node]
    closed_set = []
    navigation_map = [start_node]

    print('start node : ', (start_node.x,start_node.y), \
            '\n end node:', (end_node.x,end_node.y))

    while len(open_set) > 0 : 

        
        ## our data structure would be such that last element is always the lowest
        current_node = deepcopy(open_set.pop())
        

        if current_node.x == end_node.x and current_node.y == end_node.y:
            print('reached node')
            print([str(i) for i in navigation_map])

            break

        f_score =  current_node.g_cost + calculate_distance(current_node, end_node)
        print('current node: ',(current_node.x, current_node.y), 'f score:' , f_score)

        neighbors = find_neighbors(current_node, location_list, neighbor_distance = 200)

        ## we need to get the neighbor with the least f score and add it
        ## at the end of the open_set
        ## after that we can add the current node to the closed set

        print([str(i) for i in neighbors])
        temp_neighbor = []
        for neighbor in neighbors:

            ##navigating to each neighbor is cost of 1
            ## we will ignore neighbors where we already encountered

            if (neighbor.x,neighbor.y) in [(kk.x,kk.y) for kk in closed_set]:
                print('found ', (neighbor.x,neighbor.y), ' in ', [str(kk) for kk in closed_set])
                continue

            neighbor.g_cost = current_node.g_cost + 1
            neighbor.h_cost = calculate_distance(neighbor, end_node)
            f_neighbor = neighbor.g_cost + neighbor.h_cost
            neighbor.f_cost = f_neighbor
            print(f_neighbor)
            temp_neighbor.append(neighbor)

            # if f_neighbor < f_score:
                
            #     print('adding to open set :', neighbor.x, neighbor.y)
            #     open_set.append(neighbor)
            #     navigation_map.append(neighbor)
            
        new_list = sorted(temp_neighbor, key = lambda x: x.f_cost, reverse = False)
    
        if new_list and new_list[0].f_cost <= f_score:

            navigation_map.append(new_list[0])
            open_set.append(new_list[0])
        
        closed_set.append(current_node)
            

## lets create our sample data. forming a grid 
x = [100,100,100,100,300,300,300,300,500,500,500,500]
y = [100,200,300,400,400,300,200,100,400,200,300,100]


location_list = [Location(i,j) for i, j in zip(x,y)]
start_node = location_list[3]
end_node = location_list[-1]

find_shortest_route(start_node, end_node)
display_map(location_list, start_node, end_node)

# print(calculate_distance(Location(100,400), Location(100,200)))