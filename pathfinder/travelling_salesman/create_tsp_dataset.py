"""

this is using TSP data set from the website http://www.math.uwaterloo.ca/tsp/data/index.html
the sample below uses country Djibouti
According to website optimal path is 6656
Total number of cities is 38
this is a sizeable figure

Our code below will read the tsp.txt file.
Create locations instances out of them and create adjacency matrix as well

"""

import pandas as panda
from math import sqrt
from travel_using_ga import Population

FILE_NAME = 'dj38.tsp.txt'

class Location(object):

    def __init__(self, identifier, x, y):
        self.identifier = identifier
        self.x = x
        self.y = y

def calculate_distance(a, b):
    
    return round(sqrt(  (a.x - b.x)**2 + (a.y - b.y)**2  ))

data = panda.read_csv(FILE_NAME, delimiter=' ',skiprows=10)

header = data.columns.values

locations = []
locations.append(Location(int(header[0]), float(header[1]), float(header[2])))
data.columns = ['id','x','y']

for i in range(len(data)):

    locations.append(Location(data.iloc[i]['id'],data.iloc[i]['x'],data.iloc[i]['y']))

print(len(locations))

number_of_cities = len(locations)

adjacency_matrix= []

for count in range(number_of_cities):

    row = []

    for inner_count in range(number_of_cities):
        row.append(calculate_distance(locations[count], locations[inner_count]))

    adjacency_matrix.append(row)

print(adjacency_matrix)

cities = list(range(1,number_of_cities+1))
print(cities)



def execute_djibuouti(adjacency_matrix, number_of_djibouti_scities, sample):

    starting_point = 13

    epoch = 1000

    record = []

    for i in range(1, number_of_djibouti_scities + 1):
       
        population = Population(number = 50, \
                                dna_size = number_of_djibouti_scities, \
                                sample = sample, \
                                mutation_rate = 0.1, \
                                starting_point = i, \
                                adjacency_matrix = adjacency_matrix)

        population.populate()
        
        print('starting genetic mutations....')
        count = 1

        while True:
            
            ## recalculation fitness scores happens over new mating pool
            flag = population.calculate_fitness()
            
            if flag:
                print('Found phrase. solution found in generation: ', count)
                cost, path = population.record.get_lowest_score_and_path()
                print('Path: ', path , ' cost: ', cost)
                record.append((cost, path))
                break
        
            else:
                
                print('Existing mutation failed. Starting natural selection and cross over' )
                population.natural_selection()
        
                print('Natural selection and cross over completed. proceeding to check again')
        
            count = count + 1

    print('Finding lowest score...')
    cost = min(record, key = lambda x:x[0])

    print('minimum cost is ', cost[0], ' path is ', list(filter(lambda x: x == cost, record))[0][1])

execute_djibuouti(adjacency_matrix, number_of_cities, cities)