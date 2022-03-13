class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        return self.solve(nums,[],result)
    def solve(self,nums,target,result):
        if len(nums)==0:
            result.append(target)
            return result
        op1 = target.copy()
        op2 = target.copy() 
        op2.append(nums[0])
        nums=nums[1:]
        self.solve(nums,op1,result)
        self.solve(nums,op2,result)
        return result
        