
class Item(object):

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def getvalue(self):
        return self.value

    def getname(self):
        return self.name

    def getweight(self):
        return self.weight

    def get_value_by_weight(self):
        return self.value/self.weight

    def __str__(self):
        return '||I am ' + self.name+', with weight '+str(self.weight)+', with value '+str(self.value)+'||'

    def __repr__(self):
        return '||I am ' + self.name+', with weight '+str(self.weight)+', with value '+str(self.value)+'||'


def keep_taking_till_next(items, available_weight):
    
    if items==[] or available_weight==0:

        # we are exhausted nothing else to do
        # value returned is 0 and no items have been added
        return (0,()) 

    elif items[0].getweight() > available_weight:
        ## essentially we couldnt add the first one 
        ## so we get the ball rolling to the next item

        return keep_taking_till_next(items[1:], available_weight)
    
    ## no items have been added yet..we do a  hail mary and
    ## add the very first item and get the ball rolling
    ## ofcourse add the first one only if weight doesnt exceed
    else:
        
        print(items)
        next_element = items[0]

        #choice 1 : left tree: taking the 0th element and proceeding
        # we have taken the 0th element. so available weight decreases
        value_left, stolen_items = keep_taking_till_next(items[1:], \
                    available_weight - next_element.getweight())

        value_left = next_element.getvalue()+value_left

        #choice 2 : right tree: dont take the 0th element
        # we havnt taken the 0th element so available weight is still the total weight available
        value_right, stolen_items_right = keep_taking_till_next(items[1:], available_weight)


        if value_left > value_right:
            
            result = (value_left, (next_element,)+(stolen_items,))
        
        else:
            
            result = (value_right, stolen_items_right)

        return result





def memoize_keep_taking_till_next(items, available_weight, memo):
    '''

        essentially an optimized version where we 
        reduce the number of operations.

        if you notice, we dont really take care which
        items are selected. we only care about how many 
        items are left and the weight that it sums upto

        so if we have vase+clock and 10 weight left
        vase+radio and 10 weight left , for us they 
        are one and same.
        
        so at any point, we are dealing with a call
        with the same length of items and same weight
        remaining , we will not call that subroutine.
        we will use the memoized version

    '''

    if (len(items), available_weight) in memo:
        
        return memo[(len(items), available_weight)]

    elif items==[] or available_weight==0:

        # we are exhausted nothing else to do
        # value returned is 0 and no items have been added
        return (0,()) 

    elif items[0].getweight() > available_weight:
        ## essentially we couldnt add the first one 
        ## so we get the ball rolling to the next item

        return memoize_keep_taking_till_next(items[1:], available_weight, memo)
    
    ## no items have been added yet..we do a  hail mary and
    ## add the very first item and get the ball rolling
    ## ofcourse add the first one only if weight doesnt exceed
    else:
        
        print(items)
        next_element = items[0]

        #choice 1 : left tree: taking the 0th element and proceeding
        # we have taken the 0th element. so available weight decreases
        value_left, stolen_items = memoize_keep_taking_till_next(items[1:], \
                    available_weight - next_element.getweight(), memo)

        value_left = next_element.getvalue()+value_left

        #choice 2 : right tree: dont take the 0th element
        # we havnt taken the 0th element so available weight is still the total weight available
        value_right, stolen_items_right = memoize_keep_taking_till_next(\
                                items[1:],\
                                 available_weight, \
                                    memo)


        if value_left > value_right:
            
            result = (value_left, (next_element,)+(stolen_items,))
        
        else:
            
            result = (value_right, stolen_items_right)

        memo[(len(items), available_weight)] = result
        return result

def build_items():

    names = ['clock', 'painting','radio','vase']
    values = [6,7,8,9]
    weights = [3,3,2,5]

    items = []

    for i in range(len(names)):
        items.append(Item(names[i],weights[i], values[i]))

    return items


def execute():

    items = build_items()
    max_weight = 5
    
    results = keep_taking_till_next(items, max_weight)

    results =  memoize_keep_taking_till_next(items, max_weight, {})

    print('final results:',results)
    # print('total value:', value)

execute()
