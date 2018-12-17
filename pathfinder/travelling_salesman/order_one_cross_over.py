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


execute()