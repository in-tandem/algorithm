import random
from copy import deepcopy
import string

def one_order_cross_over(sample_a, sample_b):

    """
        the way cross over works is as follow:

        say we have two samples, sample_A  = 1,2,6,8,9,7 sample_b = 9,5,6,7,8,3

        we take a random swath of characters from sample_a / eg say 2-4 ie 6,8,9
        now we take the remaining right most characters from sample_b starting from 4/ ie 3
        we add it to the child . ie 6,8,9,3

        now we take the remaining characters from sample_b which are not in child and
        shuffling it take random remaining characters
        
        in our example, 2 characters are remaining which belongs to (5,7)
        so our child becomes 5,7,6,8,9,3
        

    """

    random_swath_begin, random_swath_end = random.randint(0, len(sample_a)//2), random.randint(len(sample_a)//2, len(sample_a))

    child = sample_a[random_swath_begin: random_swath_end] + sample_b[random_swath_end:]

    characters_remaining = random.sample(list(set(sample_b) - set(child)), len(sample_b)-len(child))

    return characters_remaining + child

class Population(object):
    
    def __init__(self, number, dna_size, sample, mutation_rate, starting_point):

        self.size = number
        self.sample = sample
        self.dna_size = dna_size
        self.dna = []
        self.mutation_rate = mutation_rate
        self.starting_point = starting_point


    def populate(self):

        sample = [i for i in self.sample if i==self.starting_point]
        [self.dna.append( DNA( [sample[i] for i in random.sample(range(len(sample)), self.dna_size)])) for i in range(self.size)]

    def natural_selection(self):
        """
            we would like to give our dnas with lowest scores (lower score means lower distance)
            higher chances. one very simple way to achieve the same would be to 
            assign score as 1/dna.fitness

            we would also normalize so that all scores are within 0 - 1

        """

        print('Starting to create a more evolved population')

        mating_pool = []
        
        total_fitness_score = sum([i.fitness for i in self.dna])
        total_fitness_score = total_fitness_score if total_fitness_score > 0 else 1

        for dna in self.dna:

            score = dna.fitness/total_fitness_score
            score = round((1/score)*100)

            [mating_pool.append(dna) for i in range(score)] if score > 0 else None

        self.reproduce(mating_pool)
        

    def reproduce(self,mating_pool):
        
        print('size of mating pool: ',len(mating_pool))
        for i in range(self.size):

                
            random_index_1 = random.randint(0,len(mating_pool)-1)
            random_index_2 = random.randint(0,len(mating_pool)-1)
            
            parent1 = mating_pool[random_index_1]
            parent2 = mating_pool[random_index_2]

            child = parent1.mate(parent2)

            self.dna[i] = child.mutate(self.sample, self.mutation_rate)

    def calculate_fitness(self, adjacency_matrix):

        for item in self.dna:
            item.calculate_fitness(adjacency_matrix)


class DNA(object):
    
    def __init__(self, gene):

        self.gene = gene if gene else []
        self.fitness = 0

    def calculate_fitness(self, adjacency_matrix):
        """

            genes in this particular dna denotes the path
            so if gene is 1,2,3,4 our fitness score would be 
            sum of distance from 1->2->3->4

        """
        
        sum = 0

        for count in range(len(self.gene)-2):
            
            sum = sum + adjacency_matrix[self.gene[count]][self.gene[count + 1]]

        sum = sum + adjacency_matrix[self.gene[-1]][self.gene[0]]

        self.fitness = sum


    def mutate(self,sample, mutation_rate):
    
        ## we cannot take from the sample cities, since it is possible that city is repeated
        self.gene[random.randint(0, len(self.gene) - 1 )] = self.gene[random.randint(0, len(self.gene) - 1 )]
        return self

    
    def mate(self, another_dna):

        return DNA(one_order_cross_over(self.gene, another_dna.gene))


def execute():

    """

        the problem with travelling salesman problem is the number of cities means the 
        number of possible paths as n!

        so if our population has 7 cities, the number of dna in our population will
        be 7!

        if we create actually that many number of population then what we are
        doing is resorting back to brute force algorithm

        we would like to create a smaller set. say a population of 4! 
        and then have our evolution give birth to that many number of combinations

        IMP: however it is important that our sample , irrespective of the number
        of various samples, each has exactly 7 cities.

        when all cities have been hit atleast one. record those paths.
        and have compare the sums.

        p.s: when do we end??
        - essentially when all combinations have been reached. how do we know all
          combinations have been reached?? 

        p.s.  how do we know we have reached the shortest route?



    """
    pass

