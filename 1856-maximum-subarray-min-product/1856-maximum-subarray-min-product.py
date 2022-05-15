class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        pref_sum = [0]
        res = 0
        for n in nums:
            pref_sum.append(pref_sum[-1]+n)
        
        for i,n in enumerate(nums):
            new_start = i
            # break monotonic inc order
            while stack and stack[-1][1] > n:
                start,val = stack.pop()
                total = pref_sum[i] - pref_sum[start]
                res = max(res,val*total)
                new_start = start
            stack.append((new_start,n))
        # here we have the monotonic inc stack
        # cal min product and find max among them
        for start,val in stack:
            total = pref_sum[len(nums)] - pref_sum[start]
            res = max(res,val*total)
        return res%(10**9 + 7)
                
                