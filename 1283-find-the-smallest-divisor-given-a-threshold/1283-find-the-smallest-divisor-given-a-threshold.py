class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = 10**6
        res = -1        
        while start <= end:
            mid = start + (end-start) //2 
            if(self.get_sum(nums,mid) > threshold):
                start = mid + 1
            else:
                res = mid
                end = mid - 1
        return res
    def get_sum(self,arr,div):
        _sum = 0
        for num in arr:
            _sum += math.ceil(num/div)
        return _sum