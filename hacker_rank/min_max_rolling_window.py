import itertools

def max_of_min_of_all_possibilities(sequence):
    
    window_sizes = range(1, len(sequence)+1)

    rolling_window_min_of_each = []

    for i in window_sizes :
    
        current = []
    
        # for j in range(len(sequence)):
            
        current.extend([sequence[j:j+i] for j in range(len(sequence)-i+1)])

        print(current)
        rolling_window_min_of_each.append(max([min(k) for k in current]))

    print('rolling wind',rolling_window_min_of_each)
    return ' '.join(map(str,rolling_window_min_of_each))

print(max_of_min_of_all_possibilities([2,6,1,12]))