class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen_at = {} # {count: index}
        seen_at[0] = -1
        res = 0
        count = 0
        for i,num in enumerate(nums):
            if num:
                count +=1
            else:
                count -=1
            
            if count in seen_at:
                res = max(res,i-seen_at[count])
            else:
                seen_at[count] = i
        return res