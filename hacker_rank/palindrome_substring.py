
def is_palindrome(sequence):

    ## palindrome checker loops over n + n times.. that is once in reverse once not    
    return True if len(sequence)>1 and sequence[::-1]==sequence else False

def is_palindrome_single_iteration(sequence):
    leftIndex = 0
    rightIndex = len(sequence) - 1

    while leftIndex < rightIndex:

        if sequence[leftIndex]!=sequence[rightIndex]:
            return False
        
        leftIndex += 1
        rightIndex -= 1
    
    return True

pattern = 'racecarenterelephantmalayalam'

def execute(pattern):

    count = 0
    results  = set()
    for i in range(len(pattern)):

        for j in range(i, len(pattern)):

            if is_palindrome(pattern[i:j+1]):
                count = count + 1 
                results.add(pattern[i:j+1])

    print(count, results)

execute(pattern)