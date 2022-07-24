class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num%10
                num = num//10
            return digit_sum
        
        digit_sum_to_number = defaultdict(list)
        max_sum = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            digit_sum_to_number[digit_sum].append(num)
            if len(digit_sum_to_number[digit_sum]) == 2:
                max_sum = max(max_sum,digit_sum_to_number[digit_sum][0]+digit_sum_to_number[digit_sum][1])
        return max_sum
            
        