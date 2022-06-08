class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minutes = []
        res = 0
        for d,s in zip(dist,speed):
            time = math.ceil(d/s)
            minutes.append(time)
        
        minutes.sort()
        for minute in range(len(minutes)):
            if minute >= minutes[minute]:
                return res
            res += 1
        return res