from collections import deque
from collections import defaultdict
from collections import OrderedDict
class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        #no access yet
        self.access_count = -1

    def __str__(self):
        return 'key :%s and value : %s and access_count %d'%(self.key, self.value, self.access_count)

    def __repr__(self):
        
        return 'key :%s and value : %s and access_count %d'%(self.key, self.value, self.access_count)

    def access(self):
        self.access_count += 1
        return self.value


class LeastFrequentlyUsedCache:
    '''

        developed with the limitation of every incoming element
        being new element

    '''

    SOME_CONSTANT_VALUE = 'some_constant'

    def __init__(self, cache_size):

        self.size = cache_size

        # queue of node elements
        self.access_count = 1

        # key will be str, value will be a node element
        self.data = {}

        self.dict_access_counter = defaultdict(OrderedDict)

    def insert(self, key, value):
        
        if self.access_count > self.size:

            #requires resizing before inserting
            #pop left most element from access queue. that has the ignominious honor
            #of being the least frequently used item
            #get the key, delete that from the dictionary
            #delete from data access counter
            
            print('cache limit reached: key %s and value %s' %(key,value))
            # least_frequently_used_counter = self.dict_access_counter[0] \
            #         if 0 in self.dict_access_counter.keys() else self.dict_access_counter[-1]

            least_frequently_used_counter = self.dict_access_counter.get(0)
            key_to_delete = 0 
            if not least_frequently_used_counter:

                least_frequently_used_counter = self.dict_access_counter[-1]
                key_to_delete = -1

            least_frequently_used_key = list(least_frequently_used_counter.keys())[0]
            
            del self.data[least_frequently_used_key]
            del self.dict_access_counter[key_to_delete][least_frequently_used_key]

        #add incoming key value pair to dict
        #add incoming key to accesscount queue.
        # we will append incoming to the right of queue
        # since it is just added, access count is also the lowest
        # however we still cannot delete it immediately since 
        # that will defeat the whole purpose of a cache
        
        node = Node(key,value)
        self.data[key] = node
        self.access_count = self.access_count + 1
        
        current_counter = self.dict_access_counter.get(-1, {})

        if current_counter:
            current_counter[node.key] = self.SOME_CONSTANT_VALUE
        else:
            self.dict_access_counter[-1] = {node.key:self.SOME_CONSTANT_VALUE}
        

    def fetch(self, key):
        
        node = self.data.get(key)

        if not node:
            raise ValueError('key %s not available'%key)

        current_access_count_of_node = node.access_count

        ## removing the element from the data access counter dict
        del self.dict_access_counter[current_access_count_of_node][key]
        
        value = node.access()

        current_node = self.dict_access_counter.get(current_access_count_of_node+1)

        if current_node:
            current_node[key] = self.SOME_CONSTANT_VALUE
        
        else:
            self.dict_access_counter[current_access_count_of_node+1] = {key:self.SOME_CONSTANT_VALUE}
        
        return value

    def remove(self,key):
        pass


def execute():
    keys = [11,22,33,44,11,11,55]
    values = ['a11','a22','a33','a44','a11','a11','a55']

    # keys = [11,22,33, 44]
    # values = ['a11','a22','a33','a44']

    cache = LeastFrequentlyUsedCache(3)

    for key, value in zip(keys,values):
        cache.insert(key,value)

    print('my cache internals:', cache.data)
    print('my cache internals counter:', cache.dict_access_counter)


execute()