class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unqiue_word = set()
        for word in words:
            code = ''
            for char in word:
                code += morse_code[ord(char)-ord('a')]
            unqiue_word.add(code)
        return len(unqiue_word)