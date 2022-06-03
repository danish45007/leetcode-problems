class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref_sum_matrix = [0]*len(nums)
        pref_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            self.pref_sum_matrix[i] = pref_sum
        print(self.pref_sum_matrix)

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum_matrix[right]-self.pref_sum_matrix[left]+self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)