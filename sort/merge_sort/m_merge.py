'''

we have seen how to merge two sorted lists in merge.py
now if there are two lists, its two way sorted
if there are 3 lists as input we have 3 way sorted
if there are m lists as imputs we have m way sorted

in this file, we will implement m way sorted

algorithm:

1. take first two and merge
2. take the result of 1 and merge with 3rd
... till no more lists are present

'''

import numpy as np
from merge import merge

def m_way_merge(m):
    '''
    :param m : expecting list of sorted lists
    '''
    total = len(m)

    if total == 1:
        return m[0]

    elif total == 2:
        return merge(m[0],m[1])

    else:
        merge_first_two = merge(m[0], m[1])
        new_input = [merge_first_two]
        new_input.extend(m[2:])
        return m_way_merge(new_input)

    


l1 = sorted(np.random.randint(1,22,(2)))
l2 = sorted(np.random.randint(1,45,(3)))
l3 = sorted(np.random.randint(33,122,(4)))
l4 = sorted(np.random.randint(33,122,(5)))

print(l1)
print(l2)
print(l3)
print(l4)

print(m_way_merge([l1,l2,l3,l4]))