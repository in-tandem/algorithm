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
# pattern = 'abacab'
# pattern = 'abcdabd'

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

create_lps_table(pattern)


    

