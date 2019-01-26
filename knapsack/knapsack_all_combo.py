'''
BRUTE FORCE
This is essentially a O(2**n) optimization of the 
knapsack problem.

we create a vector of 0s,1s, where 0 reprsent item
not selected, 1 represent item selected.
create all such vectors. 
enumerate across all and select only those which have weight 
closest to max weight given

'''


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


def create_possibilities(max_weight, items):
    
    total_items = len(items)
    all_items = {}

    for i in range(0, 2**total_items):# looping 2**n times

        possibility  = []
        total_weight = 0

        for item in items:
            
            if item.getweight()+total_weight <= max_weight:
                possibility.append(item)
                total_weight += item.getweight()

            else:
                possibility.append(None)

        if total_weight <= max_weight:
            all_items[total_weight] = possibility

    items_closest_to_max_weight = max(all_items.keys())

    items_selected = all_items.get(items_closest_to_max_weight)
    return [i for i in items_selected if i is not None]


def build_items():

    names = ['clock', 'painting','radio','vase','book','computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]

    items = []

    for i in range(len(names)):
        items.append(Item(names[i],weights[i], values[i]))

    return items

def execute():

    
    items = build_items()

    sorted_by_highest_weight = sorted(items, \
                                    key = lambda x: x.getweight(), reverse = False)

    sorted_by_highest_value = sorted(items, \
                                    key = lambda x: x.getvalue(), reverse = True)

    sorted_by_highest_value_by_weight = sorted(items, \
                                    key = lambda x: x.get_value_by_weight(), \
                                            reverse = True)
                                            
    print(create_possibilities(20, sorted_by_highest_value_by_weight))

execute()