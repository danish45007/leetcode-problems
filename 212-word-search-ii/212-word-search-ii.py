class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False
    
    def insert_into_trie(self,word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.is_end = True
    
    def word_exists(self,word):
        curr = self
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.is_end
    def prefix_exists(self,prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
    def get_root(self):
        return self.root
    def prune(self, word):
        curr = self
        stack = []
        
        for ch in word:
            stack.append(curr)
            curr = curr.children[ch]
        curr.is_word = False

        for t_node, ch in reversed(list(zip(stack, word))):
            if len(t_node.children[ch].children) > 0:  # has children
                return
            else:
                del t_node.children[ch]
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row = len(board)
        col = len(board[0])
        trie = Trie()
        # root = trie.get_root()
        # prefill words list into trie for constant look up operation
        for word in words:
            trie.insert_into_trie(word)
        res = set()
        visited = set()
        def dfs(r,c,pref,node):
            # in bound check
            if(r < 0 or c < 0 or r == row or c == col or (r,c) in visited or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            pref += board[r][c]
            
            if node.is_end:
                res.add(pref)
                trie.prune(pref)
                
            dfs(r+1,c,pref,node)
            dfs(r-1,c,pref,node)
            dfs(r,c+1,pref,node)
            dfs(r,c-1,pref,node)
            visited.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,"",trie)
        return list(res)
        
        
            
        