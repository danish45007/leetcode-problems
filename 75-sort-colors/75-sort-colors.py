class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        i = 0
        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]
        
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l +=1
            elif nums[i] == 2:
                swap(i,r)
                r -=1
                i -=1
            i +=1
        
        # hash_map = {0:0, 1:0, 2:0}
        # for num in nums:
        #     hash_map[num] = hash_map.get(num, 0) + 1
        # for i in range(hash_map[0]):
        #     nums[index] = 0
        #     index += 1
        # for i in range(hash_map[1]):
        #     nums[index] = 1
        #     index+=1
        # for i in range(hash_map[2]):
        #     nums[index] = 2
        #     index+=1
            
        