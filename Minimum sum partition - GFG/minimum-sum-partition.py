#User function Template for python3
import math
class Solution:
	def minDifference(self, nums, n):
		if(len(nums) == 2 and (nums[0] == -nums[1] or nums[1] == -nums[0])):
            return abs(nums[1]-nums[0])
            
        _sum = sum(nums)
        n = len(nums)
        search_area = []
        _min = float('inf')
        dp = [[False for j in range(_sum+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for j in range(1,_sum+1):
            dp[0][j] = False
            
        for i in range(1,n+1):
            for j in range(1,_sum+1):
                if(nums[i-1] <= j):
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        lst_row = dp[n]
        lst_row_half_size = math.floor((len(lst_row)-1) / 2)
        for i in range(lst_row_half_size+1):
            if(lst_row[i]):
                search_area.append(i)
        for i in range(len(search_area)):
            _min = min(_min,_sum-2*search_area[i])
        return _min

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends