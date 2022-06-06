class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # backtracking solution
        # O(n^2*m)
        # dp = {} #{indx,sub_set}
        # def dfs(i,m):
        #     if m == 1:
        #         return sum(nums[i:])
        #     if (i,m) in dp:
        #         print((i,m))
        #         return dp[(i,m)]
        #     curr_sum = 0
        #     res = float('inf')
        #     for j in range(i,len(nums)-m+1):
        #         curr_sum += nums[j]
        #         max_sum = max(curr_sum,dfs(j+1,m-1))
        #         res = min(res,max_sum)
        #         if curr_sum > max_sum:
        #             break
        #     dp[(i,m)] = res
        #     return res
        # return dfs(0,m)
    
    
        start = max(nums)
        end = sum(nums)
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if(self.is_valid_sub_array_sum(nums,m,mid)):
                res = mid
                end = mid -1
            else:
                start = mid + 1
        return res
    def is_valid_sub_array_sum(self,nums,m,curr_max):
        sub = 1
        _sum = 0
        for num in nums:
            _sum += num
            if(_sum > curr_max):
                sub +=1
                _sum = num
        return sub <= m