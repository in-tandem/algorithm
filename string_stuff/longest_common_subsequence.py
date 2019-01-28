main_string = 'aaabghsaadfcd'
sub_string = 'abadf'

def lcs(smaller_string, larger_string):
    
    if len(smaller_string)==0 or len(larger_string)==0:
        return 0
    
    elif smaller_string[0]==larger_string[0]:

        return 1 + lcs(smaller_string[1:],larger_string[1:])
    
    else:

        return max(
            lcs(smaller_string[1:], larger_string),
            lcs(smaller_string, larger_string[1:]),
            )


def lcs_memo(smaller_string, larger_string, memo):
    
    if len(smaller_string)==0 or len(larger_string)==0:
        return 0
    
    elif smaller_string[0]==larger_string[0]:

        value = lcs_memo(smaller_string[1:],larger_string[1:],memo)
        memo[(smaller_string,larger_string)] = 1+value
        return 1 + value
    
    else:

        lhs = (smaller_string[1:], larger_string)
        rhs = (smaller_string, larger_string[1:])

        print('lhs/rhs:',memo.get(lhs), memo.get(rhs))
        return max(
            memo.get(lhs, lcs_memo(lhs[0],lhs[1],memo)) ,
            memo.get(rhs, lcs_memo(rhs[0],rhs[1], memo))
            )



print(lcs_memo(sub_string,main_string,{}))
