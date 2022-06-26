class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sorted_start_words = set()
        for word in startWords:
            sorted_word = ''.join(sorted(word))
            sorted_start_words.add(sorted_word)
        res = 0
        for word in targetWords:
            sorted_word = ''.join(sorted(word))
            for i in range(len(sorted_word)):
                w = sorted_word[:i] + sorted_word[i+1:]
                if w in sorted_start_words:
                    res +=1
                    break
        return res
            