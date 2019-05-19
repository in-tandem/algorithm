'''
A string is said to be a special palindromic string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.

'''
import itertools

def is_special_palindrome(pattern):

    all_char_same = True if len(set(pattern)) ==1 else False
    if len(pattern)%2==0 :
        return all_char_same

    mid_character  = pattern[len(pattern)//2]
    without_mid = ''.join([i for i in list(pattern) if i!=mid_character])
    all_except_mid_same  = True if len(set(without_mid)) ==1 else False
    is_mid_diff = True if mid_character not in list(without_mid) else False

    return all_char_same or (all_except_mid_same and is_mid_diff)


def produce_combinations(pattern):

    sequence = map(lambda x: itertools.combinations(pattern,x), range(1,len(pattern)+1))
    possibilities = set([''.join(i) for i in itertools.chain.from_iterable(sequence)])
    return possibilities

def count_of_special_palindrome(pattern):

    possibilities = produce_combinations(pattern)
    count  = 0
    
    for sequence in possibilities:
    
        if is_special_palindrome(sequence) and sequence in pattern:
            print(sequence)
            count +=1
    
    print(count)
    return count + len(list(pattern))


print(count_of_special_palindrome('aaaa'))


