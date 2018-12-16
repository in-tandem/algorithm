import string
import time, datetime
import random
from copy import deepcopy

class CodeTimer:
    
    """
        Utility custom contextual class for calculating the time 
        taken for a certain code block to execute
    
    """
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (time.clock() - self.start) * 1000.0
        time_taken = datetime.timedelta(milliseconds = self.took)
        print('Code block' + self.name + ' took(HH:MM:SS): ' + str(time_taken))

class DNA(object):

    def __init__(self, mutation_rate, data):
        self.mutation_rate = mutation_rate
        self.fitness = 0
        self.data = data

    def mutate(self, sample_set):
        """
            one possible mutation could be to take characters and swap
            them over
            how do we use the mutation rate here???
            say mutation rate is 0.1. which means
            we have 10/100 chance of swapping the characters with
            a new character
        """
        for item in self.data:

            if(random.random()< self.mutation_rate): ## this code has a chance of executing self.mutation_rate times

                item = sample_set[random.randint(0, len(sample_set)-1)]
    
    def crossover(self, another_dna):

        """
        our crossover mechanism would be to take a half of characters from this dna objec
        and the remaining number of objects from given another_dna to create a new dna object
        with the all other characteristics as this particular dna. except fitness.
        fitness will be 0 since this particular dna hasnt undergone fitness evaluation yet

        """

        from_this_as_parent = self.data[0: len(self.data)//2]
        from_another_parent = another_dna.data[0: len(self.data)-len(self.data)//2 ]
        
        return DNA(self.mutation_rate, from_this_as_parent+from_another_parent)

    def calculate_fitness(self, required_data):
        """
    	    
            higher number of matches in the given required data and
            data in this dna will result in higher fitness score
            the matching will be done in sequence

        """

        
        if ''.join(self.data) == required_data:
            return True
        else:    
            self.fitness = len(list(filter(lambda x: x[0]==x[1], [(i,j) for i,j in zip(self.data,required_data)]))) * 100
            print('Comparing ',''.join(self.data),' , with required data: ', required_data, ' failed. Giving \
                        fitness score of ', self.fitness )


class Population(object):
    
    def __init__(self, mutation_rate, size, dna_size, samples):

        self.mutation_rate = mutation_rate
        self.size = size
        self.dna_sample = []
        self.dna_size = dna_size
        self.mating_pool = []
        self.samples = samples

    def calculate_fitness(self, required_data):
        """

        we calculate the fitness of each dna sample. 
        essentially we look thru all dna samples to check to see how many characters are matching with the goal word
        more characters matching are given more fitness score
        the aim is:: in the next selection of dna, we will have higher probability of selecting
        the ones with the higher fitness scores

        """

        if len(self.mating_pool) > 0 :

            print('inside mating pool')
            for count in range(len(self.mating_pool)):

                flag = self.mating_pool[count].calculate_fitness(required_data)
                
                if flag:
                    return True
        
        else:

            for count in range(self.size):

                flag = self.dna_sample[count].calculate_fitness(required_data)
                
                if flag:
                    return True
            

        return False

    def crossover(self):

        temp = deepcopy(self.mating_pool)
        self.mating_pool = []
        
        for _ in range(len(temp)):

            a = temp[random.randint(0,len(temp)-1)]
            b = temp[random.randint(0,len(temp)-1)]
            temp_dna = a.crossover(b)
            temp_dna.mutate(self.samples)
            self.mating_pool.append(temp_dna)



    def natural_selection(self):
        """
            
            essentially i did not find the required phrase yet.
            i would hence repopulate. my population this time 
            would have dna s with higher fitness scores. 
            my len(mating_pool) < len(population)

            how will natural selection work?

            1. normalize the fitness scores across all dna samples
            2. so lets say there are 10 samples, 4 higher, 3 medium, 2 low medium and 2 low scores
            3. in that case, even if i do a random selection , i will have 4/10 chances to select higher parents
            4. probability of selecting higher fitness parents in the mating pool increases
            5. however we will still have lower score parents so that we can get variations in genee pool
            6. higher variations would mean higher chances of getting actual required phrase 

        """

        temp = deepcopy(self.mating_pool)
        self.mating_pool = []

        ## as an example we will take mating pool size the 3/4th the size of population

        for _ in range(round((3*self.size)/4)):

            self.mating_pool.append(self.dna_sample[random.randint(0,self.size-1)])    


    def populate(self, target):
        '''
            create a dna sample of length size given
            essentially populate self.dna_sample,  self.size times

            what do we populate self.dna_sample with?? numbers??texts??pictures??
            we populate self.dna_sample with variations on the given argument of target
            however we wrap the target value in DNA object
            hence self.dna_sample has self.size number of DNA objects

        '''

        target_size = len(target)

        for _ in range(self.size):
            
            dna = DNA(self.mutation_rate, \
                            [target[i] for i in \
                                random.sample(range(target_size), self.dna_size)])
            print(dna.data)
            self.dna_sample.append( dna)


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

    target_phrase = 'cate'

    timer = CodeTimer('timer')    
    population_size = random.randint(10000,60000)

    with timer:

        samples = list(string.ascii_lowercase)
        target_size = len(target_phrase)
        mutation_rate = random.random()

        population = Population(mutation_rate, population_size, target_size,samples)
        population.populate(samples)
        
        print('starting genetic mutations....')

        while True:
            
            ## recalculation fitness scores happens over new mating pool
            flag = population.calculate_fitness(target_phrase)
            
            if flag:
                print('Found phrase')
                break
        
            else:
                
                print('Existing mutation failed. Starting natural selection and cross over' )
                population.natural_selection()
                population.crossover()

                print('Natural selection and cross over completed. proceeding to check again')

    print(timer.took)

execute()