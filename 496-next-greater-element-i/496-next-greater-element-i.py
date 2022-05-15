class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
            Brute Force (Acceptable on leetcode)
            Time: O(n*m) where n = len(nums2),m = len(nums1)
            Space = O(m)
        '''
        # num_index_map = {}
        # res = [-1]*len(nums1)
        # for i,num in enumerate(nums1):
        #     num_index_map[num] = i
        # for i,n in enumerate(nums2):
        #     if n in num_index_map:
        #         while i < len(nums2)-1:
        #             # nearest max
        #             if nums2[i+1] > n:
        #                 res[num_index_map[n]] = nums2[i+1]
        #                 break
        #             else:
        #                 res[num_index_map[n]] = -1
        #             i += 1
        # return res
        
        '''
            Using monotonic dec stack
            Time = (n+m)
            Space = (m)
        '''
        num_index_map = {}
        res = [-1]*len(nums1)
        for i,num in enumerate(nums1):
            num_index_map[num] = i
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                prev_val = stack.pop()
                res[num_index_map[prev_val]] = curr
            if curr in num_index_map:
                stack.append(curr)
        return res
            
                        