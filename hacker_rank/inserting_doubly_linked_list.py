
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

def sortedInsert(head, data):
    to_add = DoublyLinkedListNode(data)
    previous = head
    flag = False

    while previous:

        next = previous.next

        if previous.data > data:
            previous.prev = to_add            
            to_add.next = previous
            to_add.prev = None
            head = to_add
            # previous = next
            break

        elif next and previous.data < data < next.data:
            to_add.prev = previous
            to_add.next = next
            previous.next = to_add
            # flag = True
            break
        else:
            
            if next is None:
                to_add.prev = previous
                previous.next = to_add
                to_add.next = None                
                # break
                # previous=next
          
            previous = next
    
    return head

llist_count = [1,3,4,10]

llist = DoublyLinkedList()

for i in llist_count:
    llist.insert_node(i)

sortedInsert(llist.head,0)
print_doubly_linked_list(llist.head)
    