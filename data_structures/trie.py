class Trie:

    def __init__(self, char = None):
        self.root = '*'
        self.children = []
        self.character = char
        self.word_finised = False

    
    def add(self, word):
        
        nodes = self.children
        
        for char in word:

            found = False
            for child in nodes:
                
                if child.char == char:
                    nodes = child.children
                    found = True
                    break

            if not found:
                trie = Trie(char)
                self.children.append(trie)


    def search(self, word):
        pass





    