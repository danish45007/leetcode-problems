class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if(len(nums) == 1):return 1
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        # case1 delete from both ends
        delete_from_both_end  = len(nums) - abs(min_index-max_index) + 1
        # case2 delete from leftside only
        delete_from_left = max(min_index,max_index) + 1
        # case3 delete from rightside only
        delete_from_right = len(nums) - min(min_index,max_index)
        # return min of all 3 cases
        return min(delete_from_both_end,delete_from_left,delete_from_right)