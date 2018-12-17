import random
from copy import deepcopy
import string

class Population(object):
    
    def __init__(self, number, dna_size, sample, mutation_rate ):

        self.size = number
        self.sample = sample
        self.dna_size = dna_size
        self.dna = []
        self.mutation_rate = mutation_rate

    def populate(self):

        [self.dna.append( DNA( [self.sample[i] for i in random.sample(range(len(self.sample)), self.dna_size)])) for i in range(self.size)]

    def natural_selection(self):

        print('Starting to create a more evolved population')

        mating_pool = []

        total_fitness_score = sum([i.fitness for i in self.dna])
        total_fitness_score = total_fitness_score if total_fitness_score > 0 else 1
        
        for dna in self.dna:

            score = round((dna.fitness/self.size)*100)

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

    def calculate_fitness(self, required_data):

        for item in self.dna:
            flag = item.calculate_fitness(required_data)

            if flag:
                return True

class DNA(object):
    
    def __init__(self, gene):

        self.gene = gene if gene else []
        self.fitness = 0

    def calculate_fitness(self, required_gene):

        if ''.join(self.gene) == required_gene:
            print('My genes are ', self.gene)
            return True

        else:    
            
            self.fitness = len(list(filter(lambda x: x[0]==x[1], [(i,j) for i,j in zip(self.gene,required_gene)]))) 

            print('Comparing ',''.join(self.gene),' , with required data: ', required_gene, ' failed. Giving \
                        fitness score of ', self.fitness )


    def mutate(self,sample, mutation_rate):
        ## we cannot take from the sample cities, since it is possible that city is repeated
        self.gene[random.randint(0, len(self.gene) - 1 )] = self.gene[random.randint(0, len(self.gene) - 1 )]
        return self

    
    def mate(self, another_dna):
        mid = len(self.gene)//2
        from_this_as_parent = self.gene[0: mid ]
        from_another_parent = another_dna.gene[mid: len(self.gene)]
        
        return DNA(from_this_as_parent+from_another_parent)
