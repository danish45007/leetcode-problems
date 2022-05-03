class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        dp = {}
        def dfs(index,curr_sum):
            if index == len(arr):
                return 1 if curr_sum == target else 0
                
            if (index,curr_sum) in dp:
                return dp[(index,curr_sum)]
            
            res = dfs(index+1,curr_sum+arr[index]) + dfs(index+1,curr_sum-arr[index])
            dp[(index,curr_sum)] = res
            return res
        return dfs(0,0)
                