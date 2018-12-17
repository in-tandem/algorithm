import random

size = 6
sample = range(10)

a = random.sample(sample, size) ## list of unique elements
b = random.sample(sample, size)


random_swath_begin = random.randint(0,len(a)//2)
random_swath_end = random.randint(len(a)//2, len(a))

swath = a[random_swath_begin : random_swath_end]

print('swath begin: ',random_swath_begin, ' swath end: ',random_swath_end, ' swath: ', swath)

right_swath_b = b[random_swath_end:]

new_child = swath + right_swath_b

string_remaining = list(set(b)-set(new_child))

new_child = random.sample(string_remaining, len(b) -len(new_child)) +new_child

print('a:', a, ' b:',b, ' new_child: ', new_child)