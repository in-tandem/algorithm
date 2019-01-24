'''
in merge_sort.py what we did was:
    split the list into single size list.. since one size list if already sorted
    we then perform a m way merging

in traditional merge sort techniques :
    we split list into half
    keep splitting in halves till single size list is received
    compare and roll up to get a sorted list of same order

'''

l = [11,2,5,3,7,22,10, -9,0,1,345]
# from merge import merge

## divide and conquer merge sort algorithm
def merge_sort(l):
    
    if len(l) > 1:
        mid_point = len(l)//2 

        left = l[: mid_point]
        right  = l[mid_point:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = 0
        j = 0
        
        result = []

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                
                result.append(left[i])
                i+= 1
            
            else:
                result.append(right[j])
                j+= 1
                

        if j < len(right):
            result.extend(right[j:])

        if i< len(left):
            result.extend(left[i:])
        
        print('final sorted', result)
        return result

    else :
        return l

merge_sort(l)
