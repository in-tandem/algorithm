def find_test_indices(indices,K):
    ## find sizes of fold
    
    seq_len = len(indices)
    fold_sizes = [ seq_len//K for i in indices]
    
    for i in range(0, seq_len%K):
        fold_sizes[i] = fold_sizes[i]+1
    
    ## find the test indices
    ## start with 0, increase by fold count everytime
    
    current = 0
    for size in fold_sizes:
        start, stop = current, current + size
        yield (start,stop)
        current = stop
    
    
def solution(indices, K):
    # write your code in Python 3.6
    final_split = []
    for i in find_test_indices(indices,K):
        start, stop = i
        
        #create the training set
        training_set = indices[:start]
        training_set.extend(indices[stop:])

        if len(training_set)!= len(indices):
            final_split.append(training_set)
            
            #create the testing set    
            final_split.append(indices[start:stop])
    print(final_split)
    return final_split

solution([1,2,3,4],3)