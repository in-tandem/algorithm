
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

llist_count = [16,13,7]

llist = SinglyLinkedList()

for i in llist_count:
    # llist_item = llist_count[i]
    llist.insert_node(i)

def insertNodeAtPosition(head, data, position):
    
    count = 1
    item = head
    while item is not None:
        print(item.data, item)
        
        if count == position:
            new_data = SinglyLinkedListNode(data)
            temp = item.next
            item.next = new_data
            new_data.next = temp

        else:                
            item = item.next
        
        count = count + 1
            

insertNodeAtPosition(llist.head, 1, 2)
 