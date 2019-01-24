'''

merging is the technique where given two lists m and n which are sorted
how can you created a resultant list containing all elements of m and 
all elements of n such that the resultant list is also sorted

algorithm:

input : l1, l2. 
caveat: l1 and l2 are sorted list
output: l3 : sorted list containing all elements of l2 and l3

i,j,k = 0
index i pointing to l1[0]
index j pointing to l2[0]

if i < j:
    l3[k] = i
    i++
    k++
    # at this point we are navigating to the next element of l1. but we 
    # still are placed at the same element of l2
else:
    l3[k] = j
    j++
    k++
    # at this point we are navigating to the next element of l2. but we 
    # still are placed at the same element of l1

once all elements of a list are exhausted, be l1 or l2, simply copy the remaining
elements of the other list into l3.

the resultant l3 has all elements of l1 and l2 and is sorted as well

'''

l1 = sorted([11,22,1,2,-1,5])
l2 = sorted([3,4,1,7,22,33,121,-9,0])

def merge(s1,s2):
    result = []
    i =0
    j = 0

    while i<len(s1) and j<len(s2):

        if s1[i] <= s2[j]:
            result.append(s1[i])
            i+= 1
        else:
            result.append(s2[j])
            j+= 1
    
    if i<len(s1):
        result.extend(s1[i:])
    elif j < len(s2):
        result.extend(s2[j:])

    return result

def execute():
    print(merge(l1,l2))






