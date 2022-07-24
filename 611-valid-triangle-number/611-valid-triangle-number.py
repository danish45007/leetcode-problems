class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for a in range(len(nums)-1,1,-1):
            b,c = 0,a-1
            while b < c:
                if nums[b]+nums[c] > nums[a]:
                    res += c-b
                    c -=1
                else:
                    b +=1
        return res