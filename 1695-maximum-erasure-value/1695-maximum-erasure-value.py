class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        char_count_map = {}
        _sum,max_sum = 0,0
        l,r = 0,0
        while r <= len(nums)-1:
            char_count_map[nums[r]] = 1 + char_count_map.get(nums[r],0)
            _sum += nums[r]
            if r-l+1 == len(char_count_map):
                max_sum = max(max_sum,_sum)
            elif r-l+1 > len(char_count_map):
                while r-l+1 > len(char_count_map):
                    char_count_map[nums[l]] -=1
                    if char_count_map[nums[l]] == 0:
                        del char_count_map[nums[l]]
                    _sum -= nums[l]
                    l+=1
            r +=1
        return max_sum