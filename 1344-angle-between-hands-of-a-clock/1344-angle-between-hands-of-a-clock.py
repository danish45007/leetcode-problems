class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6*minutes
        hour_angle = 30*hour + minutes / 2
        print(hour_angle,minute_angle)
        angle_diff = abs(minute_angle-hour_angle)
        return min(angle_diff,360-angle_diff)