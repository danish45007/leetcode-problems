class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if(len(weights) < days):
            return -1
        start = max(weights)
        end = sum(weights)
        res = -1        
        while start <= end:
            mid = start + (end-start) // 2
            if(self.isValid(weights,mid,days)):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res
    def isValid(self,arr,_max,days):
        day = 1
        _sum = 0
        for i in range(len(arr)):
            _sum = _sum + arr[i]
            if(_sum > _max):
                day +=1
                _sum = arr[i]
        if(day > days):
            return False
        else:
            return True