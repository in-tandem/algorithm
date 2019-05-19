
import itertools

def is_anagram_using_itertools(pattern, pattern1):
    
    sequence = list(pattern)
    return True if pattern1 in [''.join(i) for i in itertools.permutations(sequence)] else False

def is_anagram(pattern, pattern1):
    # print(set(map(lambda x:True if x in pattern1 else False, pattern)))

    if len(pattern) >= len(pattern1):
        return False if False in set(map(lambda x:True if x in pattern1 else False, pattern)) else True

    else:
        return False if False in set(map(lambda x:True if x in pattern else False, pattern1)) else True

def produce_combinations(pattern):
    
    sequences = map(lambda x: itertools.combinations(list(pattern),x), range(len(pattern)))

    possibilities = [''.join(i) for i in itertools.chain.from_iterable(sequences) if i]
 
    return possibilities


def how_many_characters_removed(pattern1,pattern2,size1, size2):
    response = is_anagram_using_itertools(pattern1, pattern2)
    return None if not response else size1-len(pattern1)+size2-len(pattern2)

def count_of_removal_to_create_anagram(pattern1, pattern2):
    '''
        this method will return the number of characters that needs
        to be removed in order to generate anagram of the given two patterns
        
        Sample Input:
        cde
        abc

        Sample Output:
        4

        Explanation

        We delete the following characters from our two strings to turn them into anagrams of each other:

        Remove d and e from cde to get c.
        Remove a and b from abc to get c.

    '''

    possibilities_1 = produce_combinations(pattern1)
    possibilities_2 = produce_combinations(pattern2)
    size_1 = len(pattern1)
    size_2 = len(pattern2)

    count = 0 
    for sequence in possibilities_1:

        for item in possibilities_2:
            if len(item)==len(sequence):

                result = how_many_characters_removed(sequence,item,size_1, size_2)
                count = count + result if result else count

    print(count)
# print(is_anagram_using_itertools('daacb', 'acbdae'))

count_of_removal_to_create_anagram('cde','abc')