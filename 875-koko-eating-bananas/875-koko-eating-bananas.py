class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            Time: O(log(max(N)*N)) where N is size of piles
            Space: O(1)
        '''
        speed_min,speed_max = 1,max(piles)
        res = speed_max
        def can_koko_eat_in_time(speed):
            eat_time = 0
            for pile in piles:
                eat_time += math.ceil(pile/speed)
            return eat_time <= h
        while speed_min <= speed_max:
            mid_speed = (speed_min + speed_max) // 2
            if can_koko_eat_in_time(mid_speed):
                res  = min(mid_speed,res)
                speed_max = mid_speed - 1
            else:
                speed_min = mid_speed + 1
        return res
        
                
        