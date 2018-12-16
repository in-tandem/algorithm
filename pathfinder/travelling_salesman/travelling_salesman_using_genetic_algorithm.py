class DNA(object):

    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate
        self.fitness = 0

    def mutate(self):
        pass
    
    def crossover(self):
        pass

    def calculate_fitness(self):
        pass

class Population(object):
    
    def __init__(self, mutation_rate, size):

        self.mutation_rate = mutation_rate
        self.size = size
        self.dna_sample = []

    def populate(self, target):
        '''
            create a dna sample of length size given
            essentially populate self.dna_sample,  self.size times

            what do we populate self.dna_sample with?? numbers??texts??pictures??
            we populate self.dna_sample with variations on the given argument of target
            however we wrap the target value in DNA object
            hence self.dna_sample has self.size number of DNA objects

        '''
        pass


