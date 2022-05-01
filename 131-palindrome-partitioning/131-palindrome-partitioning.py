class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        def is_palindrome(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i +=1
                j -=1
            return True
        def backtrack(i):
            # out of bound case index at leaf node is gtr than i
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i,len(s)):
                # add substring to partition is the current substring is palindrome
                if(is_palindrome(s,i,j)):
                    partition.append(s[i:j+1])
                    # call the next func call for its next substring
                    backtrack(j+1)
                    partition.pop()
        backtrack(0)
        return result
            