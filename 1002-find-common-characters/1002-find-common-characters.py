class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        first = words.pop(0)
        for char in first:
            add = False
            for index, word in enumerate(words):
                if char in word:
                    words[index] = word.replace(char, '', 1)
                    add = True
                else:
                    add = False
                    break
            if add:
                result.append(char)
        return result
                    
        