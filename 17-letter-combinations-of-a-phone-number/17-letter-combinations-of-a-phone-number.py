class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digit to char map
        # constant space
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
        result = []
        def dfs(curr_digit_index,comb):
            if curr_digit_index == len(digits):
                result.append(comb)
                return
            for char in digit_to_char[digits[curr_digit_index]]:
                dfs(curr_digit_index+1,comb+char)
        if digits:
            dfs(0,'')
        return result