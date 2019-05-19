class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def get_height_of_tree(tree):
    

    dfs_stack = []
    count = 0

    current_working = tree
    dfs_stack.append(tree)
    visited = []

    while current_working:
        
        if current_working.left and current_working.left not in visited:
            dfs_stack.append(current_working.left)
            current_working = current_working.left
            visited.append(current_working)
            count = 0
            
        elif current_working.right  and current_working.right not in visited:
            dfs_stack.append(current_working.right)
            current_working = current_working.right
            visited.append(current_working)
            count = 0
        
        else:
            if dfs_stack:
                current_working = dfs_stack.pop() 
                # print('else,', current_working.info, dfs_stack)
                count = count +1
            else:
                current_working = None

        

    print('height:',len(visited), count)

    return count - 1


def execute():  

    tree = BinarySearchTree()
    t = [3 ,1,7,5,4]

    for i in t:
        tree.create(i)

    get_height_of_tree(tree.root)

execute()

