# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node: # classe do nó
    def __init__(self):
        self.nexts = {}   # filhos
        self.end = False  # fim de string?

class Trie:

    def __init__(self):
        self.root = Node() # raiz
    
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.nexts:
                current.nexts[c] = Node()
            current = current.nexts[c]
            
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.nexts:
                current = current.nexts[c]
            else:
                return False  # não encontrou uma das letras
        
        return current.end
                

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.nexts:
                current = current.nexts[c]
            else:
                return False  # não encontrou uma das letras
        
        # se ele próprio é o fim da string ou tem filhos, True...
        if current.end or len(current.nexts) > 0:
            return True
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)