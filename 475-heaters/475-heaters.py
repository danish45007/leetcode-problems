class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        def get_closest_dist(heaters,house):
            left = 0
            right = len(heaters)-1
            min_dist = float('inf')
            while left <= right:
                mid = (left+right)//2
                min_dist = min(min_dist,abs(house-heaters[mid]))
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            return min_dist
        for house in houses:
            radius = max(radius,get_closest_dist(heaters,house))
        return radius