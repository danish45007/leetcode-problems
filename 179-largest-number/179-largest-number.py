class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        def compare(n1,n2): 
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        str_nums = "".join(nums)
        return str(int(str_nums))
        