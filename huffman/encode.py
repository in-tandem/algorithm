from collections import Counter

def count_unique_elements(s):

    seq_count  = {}

    for i in s:

        seq_count[i] = seq_count.get(i, 0) + 1 

    return seq_count

class Leaf(object):

    def __init__(self, number):
        self.number = number

    def getnumber(self):
        return self.number

    def __repr__(self):
        print('I am a leaf with value:', self.number)

        return 'I am a leaf with value :' + str(self.number)

class Node(object):

    def __init__(self, left_leaf, right_leaf):
        self.rleaf = right_leaf
        self.lleaf = left_leaf
        self.sum   = right_leaf.getnumber() + left_leaf.getnumber()

    def set_left_leaf(self, leaf):
        self.lleaf = leaf
        self.sum += leaf.getnumber()

    def set_right_leaf(self, leaf):
        self.rleaf = leaf
        self.sum += leaf.getnumber()
                    
    def getnumber(self):
        return self.sum

    def __repr__(self):
        
        msg = 'I am a node'

        rmsg = ' with right node as '+ repr(self.rleaf) \
            if self.rleaf is not None else ' with no right node'

        lmsg = ' with left node as '+ repr(self.lleaf) \
            if self.lleaf is not None else ' with no left node'

        return msg + lmsg + rmsg

class Tree(object):

    def __init__(self, left_node, right_node):
        self.rnode = right_node
        self.lnode = left_node


# print(count_unique_elements('aabbccdddde'), '\n', Counter('aabbccdddde'))

## lets attempt to create a sum up tree

def build_tree(sequence, node):
    '''

    :param sequence: expecting a sorted sequence

    '''
    ## sequence is a sorted sequence in ascending order

    ## first one is a leaf
    ## second one is leaf
    ## combine both to create a node

    if len(sequence) == 0:
        return node

    elif len(sequence) == 1:
        ## theres is only one element. it will for sure be a leaf node
        ## also since its a single element left, it will be added
        ## to the incoming node, if incoming node is not present
        
        leaf = Leaf(sequence[0])

        if node is not None:

            node.set_left_leaf(leaf) if node.lleaf is None else\
                node.set_right_leaf(leaf)

            return node

        else:
            ## the only time this is possible is if
            ## we have only one element and this is the
            ## first call, hence node is none

            return Node(leaf, None)
        

    elif len(sequence)>1:

        if node is None:
            ## essentially first call,
            ## we can safely assume the first
            ## two elements are leaves and are
            ## added to node as such
            ## the remaining elements in the sequence
            ## are passed off along with the node created

            left_leaf = Leaf(sequence[0])
            right_leaf = Leaf(sequence[1])

            node = Node(left_leaf,right_leaf)

            return build_tree(sequence[2:], node)

        else:

            ## not the first call and we have some 
            ## sequence items left and we have a incoming
            ## node. at this point we have to compare and
            ## check for order of current node value
            ## remaining items in sequence
            ## remember if we have nodes, we would
            ## have left nodes already populated

            leaf = Leaf(sequence[0])
            new_node = Node(node, leaf)
            return build_tree(sequence[1:], new_node)



def execute():

    p = [2,8,9,20]
    node = None
    node = build_tree(p, node)

    print(node.getnumber())

    print(node)

execute()