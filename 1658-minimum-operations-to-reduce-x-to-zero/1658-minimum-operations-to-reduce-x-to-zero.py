class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
#         _sum = 0
#         left,right = 0,len(nums)-1
#         res = float('inf')
#         min_move = 0
#         while left < len(nums):
#             _sum += nums[left]
#             min_move +=1
#             if _sum == x:
#                 res = min_move
#                 break
#             elif _sum > x:
#                 break
#             left +=1

#         while right >= 0 and left <= len(nums) - 1:
#             if _sum + nums[right] > x:
#                 if left >= right:
#                     break
#                 _sum -= nums[left]
#                 left -=1
#                 min_move -=1
#                 if left < 0:
#                     left = len(nums) -1
#                 else:
#                     continue
#             else:
#                 _sum += nums[right]
#                 min_move += 1
#             if _sum == x:
#                 res = min(res,min_move)
#             right -=1
#         return res if res != float('inf') else -1
        def binary_search(arr, left, right, target):
            while left <= right:
                mid = (left + right) >> 1

                value = arr[mid]
                if value == target:
                    return mid

                elif value < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return -1
        
        length = len(nums)

        prefix_sum = [0] * length
        suffix_sum = [0] * length
        
        prefix_sum[0] = nums[0]
        
        for index in range(1, length):
            prefix_sum[index] += prefix_sum[index-1] + nums[index]
        
        suffix_sum[-1] = nums[-1]
        
        for index in range(length-2, -1, -1):
            suffix_sum[index] = suffix_sum[index+1] + nums[index]
        
        answer = float('inf')

        if target in prefix_sum: answer = min(answer, prefix_sum.index(target)+1)
        if target in suffix_sum: answer = min(answer, length - suffix_sum.index(target))
            
        for suffix_index in range(length-1, -1, -1):
            suffix_value = suffix_sum[suffix_index]
            prefix_index = binary_search(prefix_sum, 0, length-1, target-suffix_value)

            if prefix_index != -1 and prefix_index < suffix_index:
                current = (prefix_index+1) + (length-suffix_index) # prefix_index + 1 because arrays are 0 indexed
                answer = min(answer, current)
        return answer if answer != float('inf') else -1
        


            