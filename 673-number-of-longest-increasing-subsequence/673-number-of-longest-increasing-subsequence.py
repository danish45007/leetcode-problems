class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lis_len,res = 0,0
        for i in range(len(nums)-1,-1,-1):
            max_lis,lis_count = 1,1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    length,count = dp[j]
                    if length + 1 > max_lis:
                        max_lis = length + 1
                        lis_count = count
                    elif length + 1 == max_lis:
                        lis_count += count
            
            if max_lis > lis_len:
                lis_len,res = max_lis,lis_count
            elif max_lis == lis_len:
                res += lis_count
            
            dp[i] = [max_lis,lis_count]
        
        return res
                    