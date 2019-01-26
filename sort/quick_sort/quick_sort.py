l = [10,5,6,8,2,3,11,9,12]
# l = [11,5,6,10,9]
# l = [4,3,1]

def swap(ll, i, j):
    temp = ll[i]
    ll[i] = ll[j]
    ll[j] = temp

def partition(s, left_index, right_index):

    pivot_point = (left_index+right_index )//2
    
    pivot = s[pivot_point]
    
    i = left_index 
    j = right_index

    while True:

        while i<len(s) and s[i] <pivot:
            i+= 1

        while  j >=0 and s[j] > pivot :
            j-= 1
        
        if i >=j:
            return j 
        
        temp = s[j]
        s[j] = s[i]
        s[i] = temp

def quick_sort(s, low, high):

    if low < high:

        index = partition(s, low, high)
        quick_sort(s, low, index)
        quick_sort(s, index+1 , high)
    
    return s

print(quick_sort(l, 0 , len(l) - 1))
print('sorted list:', l)