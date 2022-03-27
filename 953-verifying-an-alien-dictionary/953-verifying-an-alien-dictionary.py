class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.char_order = {}
        for i,char in enumerate(order):
            self.char_order[char] = i
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if not self.check_two_words_in_order(w1,w2):
                return False
                break
        return True
    
    def check_two_words_in_order(self,word1,word2):
        if (len(word1) > len(word2) and word1.find(word2) != -1):
            return False
        
        for i in range(min(len(word1),len(word2))):
            if(word1[i] != word2[i]):
                print(self.char_order[word1[i]],self.char_order[word2[i]])
                if(self.char_order[word1[i]] > self.char_order[word2[i]]): return False
                if(self.char_order[word1[i]] < self.char_order[word2[i]]): return True
        return True
                