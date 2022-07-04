class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        fist_occurrence = {} #{num: index}
        last_occurrence = {} #{num: index}
        freq_count = {} #{num: count}
        
        for i in range(len(nums)):
            # check if the number is occurrencing for the first time
            if nums[i] not in fist_occurrence:
                fist_occurrence[nums[i]] = i
            last_occurrence[nums[i]] = i
            freq_count[nums[i]] = 1 + freq_count.get(nums[i],0)
        
        res = len(nums)
        max_freq = 0
        for num,count in freq_count.items():
            max_freq = max(max_freq,count)
        for num in nums:
            if max_freq == freq_count[num]:
                res = min(res,last_occurrence[num]-fist_occurrence[num]+1)
        return res
            
        
            
        