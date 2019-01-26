s = [9,-1,3,22,11,4]
# s = [-1,0,1,2]

def sort(l):
    
    for i in range(1, len(l)):

        j = i-1

        key = l[i]
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        while j >=0 and l[j] > key:
            
            l[j+1] = l[j]
            j-= 1

        l[j+1] = key

    return l
    
print(sort(s))