class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # bracktrack
        #apply dfs along all node when its the wildcard char '.'
        def dfs(start_index,root):
            curr = root
            for i in range(start_index,len(word)):
                char = word[i]
                if char == '.':
                    # get all the node at the level where level is just the indexof(word['.']) for curr
                    for child_node in curr.children.values():
                        if dfs(i+1,child_node):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end
    
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)