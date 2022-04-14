class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(e.lower() for e in s if e.isalnum())
        for i in range(len(filtered_string)):
            if filtered_string[i] != filtered_string[-1-i]:
                return False
        return True
        