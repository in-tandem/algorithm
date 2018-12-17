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
        
        # for i in range(len(self.gene)):
        #     # pick an element in x[:i+1] with which to exchange x[i]
        #     j = int(mutation_rate * (i+1))
        #     # self.gene[j] = sample[random.randint(0, len(sample) - 1 )]
        #     self.gene[i] = sample[random.randint(0, len(sample) - 1 )]
        #     # self.gene[i], self.gene[j] = self.gene[j], self.gene[i]
        self.gene[random.randint(0, len(self.gene) - 1 )] = sample[random.randint(0, len(sample) - 1 )]
        return self

    
    def mate(self, another_dna):
        mid = len(self.gene)//2
        from_this_as_parent = self.gene[0: mid ]
        from_another_parent = another_dna.gene[mid: len(self.gene)]
        
        return DNA(from_this_as_parent+from_another_parent)




def execute():
    """

        Give a set of possible combinations say 1-9 and a-z
        come up with a word which is same as the target phrase
        lets take an example of samples as a-z.
        hence there are a total of 26 possibilities
        we have a target phrase say cat.
        
        so for first letter.. possibility of c appearing is 1/26
        so for second letter..possibility of a appearing is 1/26
        so for third letter.. possibility of t appearing is 1/26

        so total possibiility of computer printing cat is 1/26*1/26*1/26 = 1/~18k
        imagine how low the probability is going to be if we increase the
        target phrase (eg say word with 38chars) or increase the sample
        sizes (say 1-9 + a-z + all ascii symbols)

        It is going to be hugeeeeeeeeeeeeeeeeeee!!!

        the lower the possibility the higher the time it will take for the computer to
        output the target phrase

    """

    target_phrase = 'caregiver'

    population_size = random.randint(50,100)

    samples = list(string.ascii_lowercase)
    target_size = len(target_phrase)
    mutation_rate = 0.1

    population = Population(population_size, target_size, samples, mutation_rate)
    population.populate()
    
    print('starting genetic mutations....')
    count = 1

    while True:
        
        ## recalculation fitness scores happens over new mating pool
        flag = population.calculate_fitness(target_phrase)
        
        if flag:
            print('Found phrase. solution found in generation: ', count)
            break
    
        else:
            
            print('Existing mutation failed. Starting natural selection and cross over' )
            population.natural_selection()
    
            print('Natural selection and cross over completed. proceeding to check again')
    
        count = count + 1

execute()