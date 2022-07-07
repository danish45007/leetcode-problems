class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(e.lower() for e in s if e.isalnum())
        start,end = 0,len(filtered_string)-1
        while start <= end:
            if filtered_string[start] != filtered_string[end]:
                return False
            start +=1
            end -=1
        return True
        