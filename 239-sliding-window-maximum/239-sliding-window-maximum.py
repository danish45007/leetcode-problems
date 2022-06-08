class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            max heap solution
            time: O(n*logn)
            space: O(n)
        '''
#         i,j = 0,0
#         res = []
#         max_in_sub = []
#         heapify(max_in_sub)
#         while j < len(nums):
#             while (len(max_in_sub) > 0 and (-1 * max_in_sub[len(max_in_sub) - 1]) < nums[j]):
#                 max_in_sub.pop(len(max_in_sub) - 1)
#             heappush(max_in_sub,-1* nums[j])
#             if (j-i+1 < k):
#                 j += 1
            
#             elif (j-i+1 == k):
#                 max_ele = -1 * max_in_sub[0]
#                 res.append(max_ele)
#                 if(max_ele == nums[i]):
#                     max_in_sub.pop(max_in_sub.index(-1*max_ele))
#                 i +=1
#                 j +=1
        
#         return res
        
        '''
            linear time solution using a double ended queue
            Time: O(n)
            Space: O(n)
        '''
        l,r = 0,0
        res = []
        queue = deque()
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.popleft()
                
            if(r-l+1) == k:
                res.append(nums[queue[0]])
                l+=1
            r+=1
        return res
                