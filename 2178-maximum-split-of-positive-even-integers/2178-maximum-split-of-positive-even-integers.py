class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        if finalSum % 2:
            return res
            
        curr_sum = 0
        curr_num = 2
        while curr_sum < finalSum:
            curr_sum += curr_num
            res.append(curr_num)
            curr_num +=2
        if curr_sum == finalSum:
            return res
        else:
            res.pop(res.index(curr_sum - finalSum))
        return res

        