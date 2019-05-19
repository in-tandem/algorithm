pattern = 'i want to reverse this string'

def reverse(pattern):

    print(' '.join(pattern.split()[::-1]))

reverse(pattern)