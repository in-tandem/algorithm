'''
create a data structure in which insert/delete/search and get random happens in
constant time O(1)

insert(x): Inserts an item x to the data structure if not already present.
remove(x): Removes an item x from the data structure if present.
search(x): Searches an item x in the data structure.
getRandom(): Returns a random element from current set of elements

hashmap can perform the first three operations in constant time.
however getting a random element, (queries are like given 10 elements i want to randomly
get the 5th, 6th or 7th element) cannot be done since hashmap doesnt support indexing
this can however be done in an arraylist.
however point 1,2,3 cannot be done in arraylist. so we will use a combination of both

elements are added as keys to hashmap. their positions are values
elements are added in hashmap and arraylist as well. insertion is always at the end of array

when , elements are removed, that particular index is swapped with index of last element of array
and last element in array is removed(why? bcoz removing from end is O(1) in array)

search is simple lookup


getrandom. np.random(len(Array)), get the value

'''
import random

class ConstantTimeData:

    def __init__(self):
        self.array = []
        self.hash_table = {}

    def insert(self, value):
        self.array.append(value)
        index = len(self.array)
        self.hash_table[value] = index - 1

    def remove(self, value):
        index_in_array = self.hash_table.pop(value)
        last_item = self.array[-1]
        self.array[index_in_array] = last_item
        self.array[-1] = value
        self.array.pop()
        
    def search(self, value):
        return self.hash_table.get(value,None)
    
    def get_random(self):
        random_index = random.randint(0,len(self.array))
        return self.array[random_index]
