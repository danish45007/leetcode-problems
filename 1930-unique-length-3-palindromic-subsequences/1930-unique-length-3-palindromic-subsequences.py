class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # * _ * where left * all char in the left side, right * all the char in the right to mid
        # to be a palindrome left * should be equal to right *
        left = set()
        # as starting from the 1 as the mid of palindrome char at 0th index should be the part of the left
        # left.add(s[0])
        res = set()
        right = {}
        for char in s:
            right[char] = 1 + right.get(char,0)
        print(right)
        for m in range(len(s)):
            right[s[m]] -=1
            # checking all char a-z in the left and right
            for i in range(26):
                char = chr(ord('a')+i)
                if char in left and right[char] >0:
                    res.add((s[m],char))
            left.add(s[m])
        return len(res)
                
                
            