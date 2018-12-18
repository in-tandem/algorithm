import random



# random_swath_begin = random.randint(0,len(a)//2)
# random_swath_end = random.randint(len(a)//2, len(a))

# swath = a[random_swath_begin : random_swath_end]

# print('swath begin: ',random_swath_begin, ' swath end: ',random_swath_end, ' swath: ', swath)

# right_swath_b = b[random_swath_end:]

# new_child = swath + right_swath_b

# string_remaining = list(set(b)-set(new_child))

# new_child = random.sample(string_remaining, len(b) -len(new_child)) +new_child

# print('a:', a, ' b:',b, ' new_child: ', new_child)


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

    random_swath_begin, random_swath_end = random.randint(1, len(sample_a)//2), random.randint(len(sample_a)//2, len(sample_a ) -2 )

    child = sample_a[random_swath_begin: random_swath_end] + sample_b[random_swath_end:]

    characters_remaining = [sample_b[0]] + random.sample(list(set(sample_b) - set(child)), len(sample_b)-len(child) - 1)


    return characters_remaining+child

def execute():

    size = 8
    sample = range(10)

    a = [1] + random.sample(sample, size) + [1] ## list of unique elements
    b = [1] + random.sample(sample, size) + [1]

    print('sample_a : ', a, ' sample_b : ', b,' child:',one_order_cross_over(a,b))

def crossover(sample_a, sample_b):

    # random_swath_begin , random_swath_end = random.randint(1, len(sample_a)//2) , \
    #                             random.randint(len(sample_a)//2, len(sample_a) - 2)

    ## using self assigned swath enders to make things easier
    random_swath_begin, random_swath_end = 8, 16

    sub_sample = sample_a[random_swath_begin: random_swath_end]
    
    sub_sample_b = [i for i in sample_b[1:len(sample_b) -1] if i not in sub_sample]

    child = [sample_a[0]] + [None]* ( len(sample_a) - 2) + [sample_a[0]]

    child[random_swath_begin: random_swath_end] = sub_sample

    if random_swath_begin != 1:
        # count = 0
        
        # for i in range(1,random_swath_begin):
        #     child[i] = sub_sample_b[count]
        #     count+=1

        child[1: random_swath_begin] = sub_sample_b[:random_swath_begin - 1 ]
    
    ## at this point, we have 0:random_swath_begin + len(sub_sample) values ready
    ## now we have to populate another total - random_swath_begin - len(sub_sample) - 1 values

    count = random_swath_end

    for i in range(random_swath_begin -1 , len(sub_sample_b) -1 ):
        child[count] = sub_sample_b[i]
        count+=1
    
    # for i in range(random_swath_begin, len(sub_sample_b) -1 ):
    #     child[count] = sub_sample_b[i]
    #     count+=1

    # child[random_swath_end:len(child)-1] = sub_sample_b[random_swath_begin:]
    if None  in child:
        print('somak')
        number_of_none = len(list(filter(lambda x: x is None, child)))
        difference = list(set(list(range(1,38))) - set(child))

        ## for each none in child, take one from the difference set and populate
        for count in range(len(difference)):
            item = difference[count]
            index = child.index(None)
            child[index] = item


    return child

# execute()
import random
sample_a = random.sample(range(39), 38)
sample_b = random.sample(range(39), 38)

sample_a = [13, 21, 36, 24, 35, 31, 8, 16, 27, 2, 1, 30, 18, 32, 7, 37, 25, 22, 19, 4, 20, 9, 17, 26, 23, 14, 10, 33, 29, 5, 15, 38, 3, 11, 12, 34, 6, 13]
sample_b = [13, 17, 29, 8, 11, 30, 6, 22, 16, 19, 33, 5, 20, 25, 3, 4, 31, 27, 18, 32, 2, 34, 23, 12, 24, 10, 1, 21, 15, 7, 36, 37, 26, 9, 14, 35, 28, 13]

for _ in range(100):
    item = crossover(sample_a,sample_b)
    print('child len: ', len(item), ' none present: ', None in item)

