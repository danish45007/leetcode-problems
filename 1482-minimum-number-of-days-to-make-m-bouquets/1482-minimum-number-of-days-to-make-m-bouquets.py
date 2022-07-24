class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start = 1
        end = max(bloomDay)
        res = -1
        if m*k > len(bloomDay):
            return -1
        def can_flower_bloom(time):
            total_flowers_streak = 0
            total_bouquets = 0
            for day in bloomDay:
                if day <= time:
                    total_flowers_streak +=1
                else:
                    if total_flowers_streak >= k:
                        total_bouquets+=1
                    total_flowers_streak = 0
                if total_flowers_streak >= k:
                    total_bouquets+=1
                    total_flowers_streak = 0
            if total_flowers_streak >= k:
                total_bouquets+=1
            return total_bouquets >= m
        while start <= end:
            mid = (start+end) // 2
            if can_flower_bloom(mid):
                res = mid
                end = mid-1
            else:
                start = mid + 1
        return res
        