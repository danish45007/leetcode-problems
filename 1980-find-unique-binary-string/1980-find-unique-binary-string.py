class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        def backtrack(i,curr):
            if i == len(nums):
                res = "".join(curr)
                return None if res in nums_set else res
            
            # backtrack part
            # 1st choice not inlucling 1 at i index
            if backtrack(i+1,curr): 
                return backtrack(i+1,curr)
            
            # including 1 at index i
            curr[i] = "1"
            if backtrack(i+1,curr): 
                return backtrack(i+1,curr)
        
        return backtrack(0,["0"]*len(nums))