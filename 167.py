class Solution(object):
    def twoSum(self, numbers, target):
        left_pointer = 0
        right_pointer = len(numbers) - 1
        
        while left_pointer < right_pointer:
            sum_ = numbers[left_pointer] + numbers[right_pointer]
            if sum_ == target:
                return [left_pointer+1,right_pointer+1]
            elif sum_ < target:
                left_pointer += 1
            elif sum_ > target:
                right_pointer -= 1
        
