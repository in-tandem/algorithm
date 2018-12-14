import numpy as np 
from matplotlib import pyplot as plot 
import pandas as panda 

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
    return np.linalg.norm(a-b)

def display_map(location_list, start_node, end_node):
    
    plot.scatter([i.x for i in location_list], [i.y for i in location_list], marker ='x')
    plot.scatter(start_node.x,start_node.y,facecolors='red',alpha=.55, s=100, label = 'start')
    plot.scatter(end_node.x,end_node.y,facecolors='green',alpha=.55, s=100, label = 'end')
    plot.title("Cities to Hit")
    plot.legend(loc='best')
    plot.show()

## we will take an optimization parameter here. since our data doesnt describe how to get the neighbors
## we will take a distance measure say 500. any other nodes within 500 in either directions are our neighbors
def find_neighbors(location, location_list, neighbor_distance = 500):

    neighbors = list(filter(\
            lambda i : location.x + neighbor_distance <= i.x or \
                        location.y + neighbor_distance <= i.y , \
                    location_list))

    return neighbors


data = panda.read_csv('all/cities.csv')

print(data.shape)
## there is a total of close to 200k cities. instead of traversing thru all
## i will just select say 50 of the above. for easier visualization and trial

data = data[0:50]

print(data.shape)

locations = []

for x, y in zip(data['X'].values,data['Y'].values ):

    ## we will round everything here. jsut for simplicity and
    ## since this is our first trial
    locations.append(Location(round(x),round(y)))

print([str(i) for i in locations])

start_node = locations[0]
end_node = locations[25]

##lets plot these values in a matplot for visualization
display_map(locations, start_node, end_node)
open_set = []
closed_set = []
came_from = []

## we start our navigation from start_node always
## we calculate our f/g/h scores at start_node
## we then calculate our f/g scores for the neighbors
while len(open_set) > 0:
    pass

print(locations[5])
neighbors = find_neighbors(locations[15], locations)

print('length : ', len(neighbors), '\n nodes:', [str(i) for i in neighbors])



    