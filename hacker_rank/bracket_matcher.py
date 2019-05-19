pattern = '{}'
pattern_1 = '{()}'
pattern_2 = '{}()'
pattern_2 = '{}([]){}'
bracket_dict = {
        '{':'}', '(':')','[':']'
    }
    
def use_stack(pattern):
    stack = []
    
    for letter in pattern:

        if letter in bracket_dict.keys():
            stack.append(letter)
    
        elif letter in bracket_dict.values():
            
            if stack and bracket_dict.get(stack[-1])==letter:
    
                last_added = stack.pop()
    
            else:
    
                return False

    return True if len(stack)==0 else False



def check_subsequent_bracket(pattern):
    size = len(pattern)
    j = size - 1
    flag = True

    for i in range(0,size-1,2):

        if i>=size:
            break

        if bracket_dict.get(pattern[i])!=pattern[i+1]:
            flag = False
            break 
    
    return flag


def find_if_bracket_matching_is_perfect(pattern):

    size = len(pattern)
    j = size - 1
    flag = True
    for i in range(0,size-1):

        if i>=j:
            break

        if bracket_dict.get(pattern[i])!=pattern[j]:
            flag = False
            break 

        j -=1
    
    return flag

# print(find_if_bracket_matching_is_perfect(pattern) or check_subsequent_bracket(pattern))
# print(find_if_bracket_matching_is_perfect(pattern_1) or check_subsequent_bracket(pattern_1))
# print(find_if_bracket_matching_is_perfect(pattern_2) or check_subsequent_bracket(pattern_2))



print(use_stack(pattern))
print(use_stack(pattern_1))
print(use_stack(pattern_2))