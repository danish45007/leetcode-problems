class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2):
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)-1,-1,-1):
            new_dp = set()
            for t in dp:
                if(t+nums[i] == target):
                    return True
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp = new_dp
        return True if target in dp else False