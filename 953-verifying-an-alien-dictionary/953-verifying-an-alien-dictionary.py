class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.char_order = {}
        for i,char in enumerate(order):
            self.char_order[char] = i
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if not self.check_two_words_in_order(w1,w2):
                return False
        return True
    
    def check_two_words_in_order(self,word1,word2):
        for i in range(len(word1)):
            # word2 is pref of word1
            if i == len(word2):
                return False
            
            # check for the diff char in word1 and word2
            if word1[i] != word2[i]:
                # check if the order word1[i] comes bofore order of word2[i]
                if self.char_order[word1[i]] > self.char_order[word2[i]]:
                    return False
                break
        return True
                