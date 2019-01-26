s = [5,2,3,-1,2,0,9,8]

def sort(l):

    for i in range(len(l)):

        # min_v = l[i]
        min_index = i
        
        for j in range(i, len(l)):

            if l[j] < l[i]:
                # min_v = l[j]
                min_index = j

        temp = l[i]        
        l[i] =  l[min_index]
        l[min_index] = temp

    return l

print(sort(s))