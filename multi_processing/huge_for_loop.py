import numpy as np 
from multiprocessing import Pool,Queue,Process 


## the below is perfect candidate for multi processing.
end_node = 198000*400

# for i in range(end_node):
#     print(i)


'''

1. we will extract out the print() function to a separate function so that it can be passed off 
    multiprocessing Pool
2. create a pool with number of workers. 
3. run pool with map() function, passing the 1.func created and the argument required to run it.    
4. with clause takes care of context cleanup 
5. using starmap to pass multiple args to a function


TODO

2. make a function that returns a value

'''

def return_me_something_baby(i):
    
    return i*i

def print_me_something_baby(i):

    print(i)

def print_me_something_baby_multiple(i,j):

    print(i*j)

route = []

if __name__ == '__main__':
    
    with Pool(20) as p:
        
        # p.map(print_me_something_baby, range(10))
        # p.imap(print_me_something_baby, range(10))
        # p.starmap(print_me_something_baby_multiple, [(i,j) for i, j in zip(range(10), range(10,20))])

        route.append(p.map(return_me_something_baby, range(20),6))


# pool = Pool()
# pool.map(print_me_something_baby, range(4))
# pool.close()
print(route)

