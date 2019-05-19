from collections import defaultdict

def put_zeros_to_left_ones_to_right(sequence):
    
    htable = defaultdict(list)
    for i in sequence:
        if i==0:
            htable[0].append(i)
        else:
            htable[1].append(i)

    list1=htable.get(0,[])
    list1.extend(htable.get(1,[]))
    print(list1)



    ##another simple explanation without using additional data structures

    num_of_zeros= sequence.count(0)
    response = []
    for i in range(num_of_zeros):
        response.append(0)

    for i in range(len(sequence)-num_of_zeros):
        response.append(1)

    print(response)


put_zeros_to_left_ones_to_right([0,1,0,0,1])