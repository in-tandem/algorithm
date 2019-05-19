'''

 creating a bst where p is parent, 2p is right child and 2p + 1 is left child

'''

class Node:

    def __init__(self,payload):
        self.payload= payload
        self.left = None
        self.right = None

    
class BST:
    
    def __init__(self):
        self.node = []
        self.root = None
        self.size = 0

    def insert(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node

        else:
            item = self.root

            while item:

                if data < item.payload and item.left is None:
                    item.left = node
                    item= None
                elif data>= item.payload and item.right is None:
                    item.right = node
                    item = None
                elif data < item.payload and item.left is not None:
                    item = item.left
                elif data>= item.payload and item.right is not None:
                    item = item.right
                else:
                    item = None

        self.size += 1

    def printInOrder(self,tree):
        '''
            traverse in this fashion
            traverse left subtree
            print root
            traverse right subtree
        '''
        if tree is not None:
            
            self.printInOrder(tree.left)
            print(tree.payload)
            self.printInOrder(tree.right)
    
    def printPostOrder(self,tree):
        '''
            traverse in this fashion
            traverse left subtree            
            traverse right subtree
            print root
        '''
        if tree is not None:
            
            self.printPostOrder(tree.left)
            self.printPostOrder(tree.right)
            print(tree.payload)
    
    def printPreOrder(self,tree):
        '''
            traverse in this fashion
            print root
            traverse left subtree            
            traverse right subtree
            
        '''
        if tree is not None:
            print(tree.payload)
            self.printPreOrder(tree.left)
            self.printPreOrder(tree.right)

    def get_height(self, tree):
        
        if tree is None:
            return 0
        
        left_height = self.get_height(tree.left)
        right_height = self.get_height(tree.right)

        if left_height > right_height:
            return 1+left_height
        else:
            return 1+right_height


tree = BST()
tree.insert(70)
tree.insert(31)
tree.insert(93)
tree.insert(94)
tree.insert(14)
tree.insert(23)
tree.insert(73)

print("completed adding elements")
# tree.printPreOrder(tree.root)
tree.printPostOrder(tree.root)
print('in order traversal:')
tree.printInOrder(tree.root)
print('height of tree:',tree.get_height(tree.root))