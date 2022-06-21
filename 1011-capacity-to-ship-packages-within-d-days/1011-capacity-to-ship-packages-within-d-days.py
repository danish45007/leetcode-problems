class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if(len(weights) < days):
            return -1
        start = max(weights)
        end = sum(weights)
        res = -1        
        while start <= end:
            mid = start + (end-start) // 2
            if(self.can_ship_in_d_days(weights,mid,days)):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res
    def can_ship_in_d_days(self,weights,max_weight,days_have):
        days_taken = 1
        curr_wright = 0
        for weight in weights:
            curr_wright += weight
            if(curr_wright > max_weight):
                days_taken += 1
                curr_wright = weight
        return days_taken <= days_have