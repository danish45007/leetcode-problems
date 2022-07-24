class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.current_sum = 0
        for wt in w:
            self.current_sum += wt
            self.prefix_sum.append(self.current_sum)
        self.currrent_sum = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        # random possible value
        random_target_value = random.uniform(0,self.currrent_sum)
        # need to find the index of the <random_target_value> from our prefix_sum using binary search
        left = 0
        right = len(self.prefix_sum)-1
        res = -1
        while left <= right:
            mid = (left+right)//2
            if self.prefix_sum[mid] < random_target_value:
                left = mid+1
            else:
                res = mid
                right = mid-1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()