'''

keep iterating elements from left to right
swap if elements are not in order
keep iterating till there are no more swapping left


obviously complexity is n**2. since every element
has to be compared with every other element

worst case complecity : reversed sorted list
best case complexity : list already sorted.in that case O(n) complexity

bubble sort is better performing than most 


'''

s = [9,23,3,1 ,-1,22,198,0,1,2,2]

def swap(sequence, i, j):
    temp = sequence[i]
    sequence[i] = sequence[j]
    sequence[j]  = temp

def sort(l):

    while True:
        #keep iterating
        count = 0 # number of swaps done in one total iteration
    
        for i in range(len(l) - 1) :
            if l[i] > l[i+1]:
                swap(l, i, i+1)
                count+= 1

        if count == 0:

            break
    
    return l


print(sort(s))