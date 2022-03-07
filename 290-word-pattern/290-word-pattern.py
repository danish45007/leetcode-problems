class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        char_word_map = {}
        word_char_map = {}
        if len(words) != len(pattern):
            return False
        
        for char,word in zip(pattern,words):
            if char in char_word_map and char_word_map[char] != word:
                return False
            if word in word_char_map and word_char_map[word] != char:
                return False
            char_word_map[char] = word
            word_char_map[word] = char
        return True
                