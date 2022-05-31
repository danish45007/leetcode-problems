class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # {rem:indx}
        remainder_map = {0:-1} # initalizing with 0 to avoid the the first element being divisble by k edge case
        total = 0
        for i,n in enumerate(nums):
            total += n
            rem = total % k
            if rem not in remainder_map:
                remainder_map[rem] = i
            elif i - remainder_map[rem] > 1:
                return True
        return False