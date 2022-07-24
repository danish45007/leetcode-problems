class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        
        # check if the number is in dec. order
        # not possible to get N.G.E
        ptr_1 = len(nums)-2
        while ptr_1 >= 0 and nums[ptr_1] >= nums[ptr_1+1]:
            ptr_1 -=1
        if ptr_1 == -1:
            return -1
        ptr_2 = len(nums)-1
        while nums[ptr_1] >= nums[ptr_2]:
            ptr_2 -=1
        # swap element 
        nums[ptr_1],nums[ptr_2] = nums[ptr_2],nums[ptr_1]
        nums[ptr_1+1:] = nums[ptr_1+1:][::-1]
        res = ''
        for n in nums:
            res += str(n)
        res = int(res)
        return res if res < 2**31 else -1
        
            
        