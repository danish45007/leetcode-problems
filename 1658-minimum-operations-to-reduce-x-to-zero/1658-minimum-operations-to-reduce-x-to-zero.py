class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        _sum = 0
        left,right = 0,len(nums)-1
        res = float('inf')
        min_move = 0
        while left < len(nums):
            _sum += nums[left]
            min_move +=1
            if _sum == x:
                res = min_move
                break
            elif _sum > x:
                break
            left +=1
        
        while right >= 0 and left <= len(nums) - 1:
            if _sum + nums[right] > x:
                if left >= right:
                    break
                _sum -= nums[left]
                left -=1
                min_move -=1
                if left < 0:
                    left = len(nums) -1
                continue
            else:
                _sum += nums[right]
                min_move += 1
            if _sum == x:
                res = min(res,min_move)
            right -=1
        return res if res != float('inf') else -1
            