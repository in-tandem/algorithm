'''
priority queue is a queue data structure in which the highest priority item is removed first
as opposed to first added item as done in a normal queue
in a priority queue the logical order of items inside a queue is determined by their priority. 
The highest priority items are at the front of the queue and the lowest priority items are at the back. 
so when we dequeue, or remove an item, we remove from the head(bcoz of queue) and we get the
highest priority item

when we enqueue (add) an item, it is possible that it will move all the way up to the
head since it may be the higest priority.(low value)

we can maintain this using a list, where adding n elements to list takes o(n) time
and sorting it (in the order we want) takes O(nlogn) time.

in order to implement a priority queue , we will use a heap tree since it allows us
O(log n) operations. this is average case scenario: bcoz of tree implementation and
restriction that each parent have higher order children we keep reducing operation
size into half..hence logn

in order to implement the same we will use a normal list. keeping two things in mind

1. we will create a complete tree.. in the sense each node will have both its children as much as possible.
this might not be possible in the leaf nodes.

2. at every insertion we maintain the heap order. which is.. child nodes have to be larger than the parent node

the advantage of ensuring part 1 is that we can easily get its parents. if n is a child, 
the parent node is n//2, where n is position in the list

'''


class PriorityQueue(object):

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, element):
        self.heap.append(element)
        self.size = self.size + 1 # we dont do self.sie =len(Self.heap) so that we dnt hae to take cae of zero index eveyr time
        self.rearrange()

    def rearrange(self):
        '''
        this is the heap tree re arrangement method.
        this ensures that at every addtion our heap order is
        not broken. ie. we still have a tree where every root
        is smaller than its children

        '''
        index = self.size
        
        while index//2 > 0:
            
            if self.heap[index] < self.heap[index//2]:

                # we need to swap parents and children

                temp = self.heap[index]
                self.heap[index] = self.heap[index//2]
                self.heap[index//2] = temp

            ## we nagivate a root up..so parent is at n//2 index
            index = index//2


    def get_min_child_index(self,rootindex):
        '''
            given a root, finds its two children
            and returns the index of the minimum
            of those two children

            given a rootindex, two children are at rootindex*2
            and rootindex*2+1. in case of leafy levels, it is 
            possible that rootindex*2+1 does not exist, in which
            case we return rootindex*2

        '''
        if rootindex * 2 + 1 > self.size:
            return rootindex * 2
        else:
            return rootindex*2 if self.heap[rootindex*2] < self.heap[rootindex*2+1] else rootindex*2+1

    def push_down(self, index):
        '''
            given a particular index, we keep pushing 
            down the root(ie given index) till we 
            are back at maintainig the heap order 
        '''


        while (index * 2) <= self.size:
            
            mc = self.get_min_child_index(index)

            if self.heap[index] > self.heap[mc]:
                
                tmp = self.heap[index]
                self.heap[index] = self.heap[mc]
                self.heap[mc] = tmp
            
            index = mc

    def dequeue(self):
        '''
        it is easy to remove the highest priority item first
        since our highest priority is at the head.
        however , we would to reassign a head and make sure we 
        always follow the part 1 and 2 of the algorithm

        '''

        response = self.heap[1]

        #take the last item in the list and assign it to head
        new_head = self.heap[self.size]

        self.heap[1] = new_head

        #reduce size since one item has been removed
        self.heap.pop()
        self.size = self.size - 1

        self.push_down(1)

        return response


    def buildheap(self,alist):
        
        i = len(alist) // 2
        
        #simply add all elements to the heap
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]

        ## for each item starting from mid of the list
        ## keep pushing down the elements till order maintained
        while (i > 0):
            self.push_down(i)
            i = i - 1