class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        size = len(nums)
        odd_pref_sum = [0]*size
        even_pref_sum = [0]*size
        odd_sum,even_sum = 0,0
        # popluating sum values in odd,even pref sum array
        for i in range(size):
            # odd
            if i % 2 != 0:
                odd_sum += nums[i]
            else:
                even_sum += nums[i]
            odd_pref_sum[i] = odd_sum
            even_pref_sum[i] = even_sum

        # check for each element if removing that make odd sum equal to even sum
        count = 0
        for i in range(size):
            if i == 0:
                odd_sum_not_at_0 = even_pref_sum[-1] - even_pref_sum[i]
                even_sum_not_at_0 = odd_pref_sum[-1] - odd_pref_sum[i]
                if odd_sum_not_at_0 == even_sum_not_at_0:
                    count +=1
            else:
                odd_sum_not_at_i = odd_pref_sum[i-1] + (even_pref_sum[-1]-even_pref_sum[i])
                eve_sum_not_at_i = even_pref_sum[i-1] + (odd_pref_sum[-1]-odd_pref_sum[i])
                if odd_sum_not_at_i == eve_sum_not_at_i:
                    count +=1
        return count
            