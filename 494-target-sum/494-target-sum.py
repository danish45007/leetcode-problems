class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        arr_sum = sum(arr)
        if(len(arr) == 1 and target > arr[0] or (arr_sum + target) % 2 != 0 or abs(target) > arr_sum):
            return 0
        target_sum = (arr_sum + target) // 2
        n = len(arr)
        dp = [[0 for j in range(target_sum+1)] for i in range(n+1)]
        dp[0][0] = 1
        for j in range(1,target_sum+1):
            dp[0][j] = 0
        for i in range(1,n+1):
            for j in range(target_sum+1):
                if(arr[i-1] > j):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
        return dp[n][target_sum]