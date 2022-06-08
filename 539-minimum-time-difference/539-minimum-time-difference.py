class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # converting timestamp into normalized minute format
        minute_times = []
        for t in timePoints:
            hour,minute = t.split(':')
            minute_time = int(hour)*60+int(minute)
            minute_times.append(minute_time)
        
        minute_times.sort()
        min_diff = 1440 + minute_times[0] - minute_times[-1]
        for i in range(1,len(minute_times)):
            min_diff = min(min_diff,minute_times[i]-minute_times[i-1])

        return min_diff