class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        min_num,max_num = min(nums),max(nums)
        num_size,total_buckets = len(nums),len(nums)-1
        bucket_size = math.ceil((max_num-min_num)/total_buckets)
        max_bucket = [float('-inf')]*(total_buckets)
        min_bucket = [float('inf')]*(total_buckets)
        # populating min and max buckets with nums
        for i in range(num_size):
            if nums[i] == min_num or nums[i] == max_num:
                continue
            idx = (nums[i]-min_num)//bucket_size
            max_bucket[idx]  = max(max_bucket[idx],nums[i])
            min_bucket[idx]  = min(min_bucket[idx],nums[i])
        max_diff = 0
        for i in range(len(min_bucket)):
            if max_bucket[i] == float('-inf'):
                continue
            else:
                max_diff = max(max_diff,min_bucket[i]-min_num)
                min_num = max_bucket[i]
        return max(max_diff,max_num-min_num)
        
        
            