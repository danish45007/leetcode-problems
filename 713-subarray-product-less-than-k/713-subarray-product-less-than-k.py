class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        res = 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            if product >= k:
                while product >= k and left <= right:
                    product = product/nums[left]
                    left +=1
            res += right-left+1
            right +=1
        return res