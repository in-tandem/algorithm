'''
given a pattern of x and y, find the x and y in a given string
eg xxyxxy, gogopowerrangergogopowerranger
x = go
y = powerranger
assumption , there will be never be more than one possibility of x,y. ie (a,b) is true and (aa,bb) is true
is not possible

'''
from collections import Counter

def getMetaDataInformation(pattern):

    meta  = {}

    c = Counter(pattern)
    meta['x'] = c.get('x')
    meta['y'] = c.get('y')
    meta['start_of_y'] = pattern.find('y')

    return meta



def formStringFromPattern(pattern, y, x):
    response = []

    for i in pattern:
        if i == 'x':
            response.append(x)
        else:
            response.append(y)

    return ''.join(response)

def getNewPattern(pattern):
    
    return ''.join(map(lambda x:'x' if x=='y' else 'y', pattern)) if pattern[0]!='x' else pattern
    
def findPattern(pattern, string):
    
    

    newPattern = getNewPattern(pattern)

    metaData = getMetaDataInformation(newPattern)
    didSwitch = newPattern!=pattern

    size = 1

    while size < len(string):

        if 'y' not in newPattern:
            
            size_of_x = int(len(string )/metaData.get('x'))
            x = string[:size_of_x]

            if ''.join(map(lambda xx: x, newPattern)) == string:
                return [x,''] if not didSwitch else ['',x]

        else:
        
            size_of_y = int((len(string) - metaData.get('x') * size )/metaData.get('y'))

            start_index_of_y = metaData.get('start_of_y') * size

            y = string[start_index_of_y:start_index_of_y+size_of_y]

            formed_string = formStringFromPattern(newPattern, y, string[:size])

            if formed_string == string:
                print(formed_string)
                return [string[:size], y] if not didSwitch else [y, string[:size]]

        size += 1
    
    return []



# print(findPattern('xxyxxy','gogopowerrangergogopowerranger'))

# print(findPattern('yxyx','abab'))

# print(findPattern('xyx','abab'))

print(findPattern('yxyyyxxy','baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom'))