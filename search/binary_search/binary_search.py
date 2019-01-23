sequence1 = [34,12,11,10,1,23,44]

sequence1 = sorted(sequence1)

def binary_search(sequence, element):

    total_size = len(sequence)
    mid_point = total_size//2

    # return True if mid_point == 0 and sequence[mid_point]==element else False
    if mid_point==0 and sequence[mid_point] == element:
        return True

    elif mid_point >  0 :
        
        if element == sequence[mid_point] :

            return True

        elif element < sequence[mid_point]:

            return binary_search(sequence[0:mid_point], element)

        elif element > sequence[mid_point]:

            return binary_search(sequence[mid_point:], element)
        
        else:

            return False
    else:
        return False

print(binary_search(sequence1, 23))


print(binary_search(sequence1, -23))


print(binary_search(sequence1, 43))

