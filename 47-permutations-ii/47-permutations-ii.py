class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,perm = [],[]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        def backtrack():
            # base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
                
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -=1
                    backtrack()
                    # clean up
                    count[n] +=1
                    perm.pop()
                
        
        backtrack()
        return res
                