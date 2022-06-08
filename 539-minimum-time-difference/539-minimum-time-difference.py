class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # converting timestamp into normalized minute format
        for i,t in enumerate(timePoints):
            hour,minute = t.split(':')
            minute_time = int(hour)*60+int(minute)
            timePoints[i] = minute_time
        
        timePoints.sort()
        min_diff = 1440 + timePoints[0] - timePoints[-1]
        for i in range(1,len(timePoints)):
            min_diff = min(min_diff,timePoints[i]-timePoints[i-1])

        return min_diff