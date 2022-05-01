class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = []
        subset = []
        max_len = 0
        def backtrack(i):
            if i == len(arr):
                result.append(''.join(subset.copy()))
                return
            
            # include
            subset.append(arr[i])
            backtrack(i+1)
            
            # don't include
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        for sub in result:
            if len(list(set(sub))) == len(sub):
                max_len = max(max_len,len(sub))
        return max_len