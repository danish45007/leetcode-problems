class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_duration = 0
        for time in range(len(timeSeries)-1):
            total_duration += min(timeSeries[time+1]-timeSeries[time],duration)
        return total_duration + duration