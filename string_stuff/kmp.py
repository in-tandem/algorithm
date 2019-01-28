string = 'banananobano'
pattern = 'nano'


string = 'abceabcd'
pattern = 'abcde'

# in the below case we look for pattern in n lenght string.
# pattern matches all but the last letter b. so
# our complexity will be O(mn) (all m looked for entire n length)

string = 'aaaaaaaaaaaaaaaaa'
pattern = 'aaaab'

def brute_force_search(sequence, pattern):

    sequence_index = 0
    total_pattern_length = len(pattern)

    while sequence_index < len(sequence):

        count = 0

        # we require the temp index because whenever we encounter a non match
        # we need to backtrack to the last element in main string that was checked
        # and increment by one

        temp = sequence_index

        for j in pattern:
            
            if temp < len(sequence) and j == sequence[temp] :
        
                count+= 1
                temp += 1
        
                if count == total_pattern_length:
                    return True 
            else:
                break

        sequence_index += 1

    return False


# print(brute_force_search(string, pattern))

pattern = 'bababd'
pattern = 'ababd'
pattern = 'cbabacbd'
pattern = 'cbababcd'
# pattern = 'abcdfab'
pattern = 'abacab'
# pattern = 'abcdabd'
pattern = 'AABAACAABAA'

def create_lps_table(pattern):
    ## essentially the length of longest prefix which
    ## which is also a suffix
    ## lps[i] = length of longest prefix in pattern[0...i]which is also a suffix  of pattern[0...i]
          
    current_count =  0
    
    #first element in pattern has obviously not been repeated yet, so 0
    lps_table = [current_count]
    
    i = 1 #starting from 2nd element

    while i< len(pattern):
        
        count = 0 #length of prefix which is also a suffix
        
        k = i        
        
        while k>=1: #if k is taken till 0 then we are matching entire string with entire string and that is wrong
            
            #at first go, only check for that single element
            # then check for sequence, ie.last 2 elements(suffix),
            # last 3 elements(suffix) so on and so forth

            suffix = pattern[i] if k==i else pattern[k:i+1]
            print('i:',i, ' pattern[:i+1]:', pattern[:i], ' suffix:', suffix)

            if pattern[:i].startswith(suffix):
                count = len(suffix)
            
            k -=1

        lps_table.append(count)

        i += 1
    
    print(lps_table)

    return lps_table

# create_lps_table(pattern)


    
def kmp(sequence, pattern):
    '''
        say, 1000th character of sequence did not match with the 999th character of pattern
        we know that at this point, 999characters already matched in the sequence. we are done
        checkin them.we do not back track in the main sequence

        what do we do when we encounter a mismatch?

            1. we go back to the last matched character in pattern. so p[1000-1]
            2. we check the lps table at this point
            3. lps table will tell us where to go back
            4. so we start checking the pattern from that point onwards
        
        why??whyy 4????
        lps table has information on suffix/prefix count. 
        so 
        if lps[k] value = 1, it means pattern[0:1] is same as last  character of pattern
        if lps[k] value = 2, it means pattern[0:2] is same as last two character of pattern



    '''
    lps_table = create_lps_table(pattern)

    i = 0

    while i < len(sequence):

        j = 0

        while j < len(pattern):

            if j == 0 and pattern[0] == sequence[i]:
                i += 1
                j += 1
            
            elif j == 0 and pattern[0]!=sequence[i]:
                i += 1
                break
            
            elif pattern[j] == sequence[i]:
                j += 1
                i += 1
            
            else:
                #why lookup j-1 in lps table and not j. 
                #bcoz if j >0 it means that so far our strings have matched
                #so we go back one step, at the last matching unit in pattern
                j = lps_table[j - 1]

        if j == len(pattern) :
            
            print('entire pattern matched')
            
            return True

    return False

seq = 'abababd'
pattern = 'ababd'

print(kmp(seq, pattern))

