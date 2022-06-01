class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_amount(house):
            house = house + [0] + [0]
            for i in range(len(house)-3,-1,-1):
                house[i] = max(house[i+1],house[i+2]+house[i])
            return house[0]
        
        return max(nums[0],max_amount(nums[0:-1]),max_amount(nums[1:]))
    
        