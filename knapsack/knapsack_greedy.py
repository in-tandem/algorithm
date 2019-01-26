'''
    greedy method for 0/1 (is the objects cannot be divided, you can either add it in
    knapsack or you cant. there is no taking 2/3rds of object, eg)
    says:
    kepp taking the onces which are immediately apparently as leading to highest profit

    greedy programming technique is exactly this:
        taking local minima in the hope that it leads to our global minima

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

def build_items():

    names = ['clock', 'painting','radio','vase','book','computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]

    items = []

    for i in range(len(names)):
        items.append(Item(names[i],weights[i], values[i]))

    return items

def greedy(max_weight,items):
    '''
        based on the sorted ordering of items
        we are greedy either based on weight of
        object or value of object or value/weight ration
        of object.
        we take each ensuring that the weight max parameter
        is not exceeded

    '''
    stolen_items = []
    total_weight_in_knapsack = 0

    for item in items:
        if total_weight_in_knapsack == max_weight:
            break    
        if total_weight_in_knapsack + item.getweight() <= max_weight:
            stolen_items.append(item)
            total_weight_in_knapsack+= item.getweight()


    return stolen_items    

def execute():
    
    items = build_items()

    sorted_by_highest_weight = sorted(items, \
                                    key = lambda x: x.getweight(), reverse = False)

    sorted_by_highest_value = sorted(items, \
                                    key = lambda x: x.getvalue(), reverse = True)

    sorted_by_highest_value_by_weight = sorted(items, \
                                    key = lambda x: x.get_value_by_weight(), \
                                            reverse = True)
                                            
    # print(sorted_by_highest_weight) 
    print(greedy(20, sorted_by_highest_value_by_weight))

execute()



