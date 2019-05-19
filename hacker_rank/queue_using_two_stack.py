'''
A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.

'''
# from queue import deque

class MyQueue(object):

    def __init__(self):
        self.lifo = []
        self.fifo = []
    
    def peek(self):
        return self.fifo[0]
        
    def pop(self):
        value = self.lifo.pop()
        self.fifo.remove(0)
        return value

    def put(self, value):
        self.lifo.append(value)
        self.fifo.append(value)
