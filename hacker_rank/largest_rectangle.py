##https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import itertools

sequence = [1,2,3,4,5]
# sequence = list(range(1000))

# def find_area()
def produce_combinations_preserving_order(sequence):
    response = []
    largest_rectangle  = []
    memo = {}

    for i in range(len(sequence)):
        j = len(sequence) 
        while j > i:
            value = sequence[i:j]
            response.append(value)
            j -=1

            largest_rectangle.append(len(value)*min(value))
    
    print(response)
    # print(max(largest_rectangle))


def produce_combinations_faster(sequence):
    
    largest_rectangle = []
    memo  = {}

    for i,j in itertools.combinations(range(len(sequence)+1),2):
        value = sequence[i:j]

        if  not memo.get(value):
            memo[value] = 1
            
            largest_rectangle.append(len(value)*min(value))

    print(max(largest_rectangle))



produce_combinations_preserving_order(sequence)