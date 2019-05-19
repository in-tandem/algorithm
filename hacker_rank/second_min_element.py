import sys

def min_second_largest(sequence):

    ## this will depend on sorting algo time complexity. essentially nlogn
    sorted_sequence=sorted(list(sequence))
    print(sorted_sequence.pop(1))

    min_value ,second_min_value = (sys.maxsize,sys.maxsize)

    for i in sequence:
        if i<min_value:            
            second_min_value = min_value
            min_value = i
        elif i < second_min_value and i != min_value:
            second_min_value = i

    print(min_value)
    print(second_min_value)

min_second_largest([22,11,4,5,222,33,44,55,66,77,7])
min_second_largest(range(9))