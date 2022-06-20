class Solution:
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # res = []
        # products.sort()
        # l,r = 0,len(products)-1
        # for i in range(len(searchWord)):
        #     char = searchWord[i]
        #     while l <= r and (len(products[l]) <= i or products[l][i] != char):
        #         l +=1
        #     while l <= r and (len(products[r]) <= i or products[r][i] != char):
        #         r -=1
        #     # have the matching prefix
        #     res.append([])
        #     matching_words = r-l+1
        #     for j in range(min(3,matching_words)):
        #         res[-1].append(products[l+j])
        # return res
        class TrieNode:
            
            def __init__(self):
                self.children = {} 
                self.is_end = False

        class Trie:

            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                curr = self.root
                for w in word:
                    if w not in curr.children:
                        curr.children[w] = TrieNode()
                    curr = curr.children[w]   
                curr.is_end = True

            def searchNode(self, prefix):
                cur = self.root
                for p in prefix:
                    if p not in cur.children.keys():
                        return None
                    cur = cur.children[p]
                return cur
    
            def dfs(self, cur, result, prefix):
                if len(result) == 3:
                    return result
                if cur.is_end:
                    result.append(prefix)
                for k, v in cur.children.items():
                    self.dfs(v, result, prefix+k)
                    
        products.sort()
        t = Trie()
        for p in products:
            t.insert(p)
        
        prefix = ''
        output = []
        for c in searchWord:
            prefix += c
            cur = t.searchNode(prefix)
            result = []
            if cur:                
                t.dfs(cur, result, prefix)
            output.append(result)
        return output