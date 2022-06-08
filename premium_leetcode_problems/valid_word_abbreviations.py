'''

Description
Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

Example
Example 1:

Input : s = "internationalization", abbr = "i12iz4n"
Output : true
Example 2:

Input : s = "apple", abbr = "a2e"
Output : false

'''


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            abbr_char = abbr[abbr_ptr]
            if abbr_char.isdigit():
                # check if leading zero
                if abbr_char == "0":
                    return False
                step = 0
                # get the integer in abbr
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    step = step*10 + int(abbr[abbr_ptr])
                    abbr_ptr +=1
                word_ptr += step
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr +=1
                abbr_ptr +=1
        return word_ptr == len(word) and abbr_ptr == len(abbr)
                
