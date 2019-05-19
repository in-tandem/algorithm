from collections import defaultdict

def first_non_repeating(sequence):
    
    first_non_repeating_char = [sequence[0]]

    ## not in has O(n) complexity so below operation is o(n**2)
    for i in sequence[1:]:
        if i not in first_non_repeating_char: #and i not in open_set:
            first_non_repeating_char.append(i)

        else:
            first_non_repeating_char.remove(i)
    

    open_dict = defaultdict(lambda :0)

    for i in sequence:
        open_dict[i]= open_dict[i]+1
    
    print(open_dict)

    for i in sequence:
        if open_dict.get(i) == 1:
            print("first non repeating:"+str(i))
            break

    print(first_non_repeating_char, first_non_repeating_char[0])



first_non_repeating([3,6,3,6,5,4,5,7,4])
first_non_repeating([9, 4, 9, 6, 7, 4])
first_non_repeating([1,1,1,1,1,12,1,2])