import itertools 

possibilities = ['go','bat','me','eat','goal','boy','run']

def create_words(sequence):
    size= len(sequence)
    extras = []
    extras.extend(map(lambda x: ["".join(i) for i in itertools.permutations(sequence,x)], range(1,size)))

    # extras = map(lambda x: "".join(x),extras)

    print(extras)

    for i in possibilities:
        if i in itertools.chain.from_iterable(extras):
            print('found word:', i)


    ##since possibilities size is lesser than sequence permutations we will scan the possibilities
    ## and check if we are able to form the words
    for i in possibilities:
        count_of_letters = 0
        for letter in i:
            if letter in sequence:
                count_of_letters +=1
            else:
                break
        
        if count_of_letters == len(i):
            print('found word in possibilities and sequence:', i)

        

create_words(['e','o','b','a','m','g','l'])