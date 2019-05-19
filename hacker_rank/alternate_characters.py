'''

You are given a string containing characters A and B only. Your task is to change it into a string 
such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string s = AABAAB , remove A an  at positions 0 and 3 to make ABAB  in 2 deletions.

'''

def alternatingCharacters(sequence):

    l=len(sequence)
    count=1
    for i in range(len(sequence)-1):
        if sequence[i]!=sequence[i+1]:
            count+=1
        
    return l-int(count)

print(alternatingCharacters('AABAAB'))