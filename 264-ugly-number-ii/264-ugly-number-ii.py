class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        by_two_position = by_three_position = by_five_position = 0
        while len(ugly_numbers) < n:
            multiple_by_two = ugly_numbers[by_two_position] * 2
            multiple_by_three = ugly_numbers[by_three_position] * 3            
            multiple_by_five = ugly_numbers[by_five_position] * 5
            
            min_position = min(multiple_by_two,multiple_by_three,multiple_by_five)
            ugly_numbers.append(min_position)
            
            if min_position == multiple_by_two:
                by_two_position += 1
            
            if min_position == multiple_by_three:
                by_three_position += 1
            
            if min_position == multiple_by_five:
                by_five_position += 1
        return ugly_numbers[-1]