class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": 'wxyz'
        }
        
        res = []
        def back_track(i,curr_string):
            if len(curr_string) == len(digits):
                res.append(curr_string)
                return
            for char in digit_to_char[digits[i]]:
                back_track(i+1,curr_string+char)
        if digits:
            back_track(0,"")
        return res