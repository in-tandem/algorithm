def sort(sequence):
    temp_stack = []
    
    while len(sequence) > 0:
        item = sequence.pop()

        if not temp_stack:
            temp_stack.append(item)
        
        elif item < temp_stack[-1]:
            
            temp_stack.append(item)
        
        else:
            temp_stack.append(item)



