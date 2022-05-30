class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m_sum = sum(rolls)
        n_sum = (m+n)*mean - m_sum
        res = []
        if n_sum < n or n_sum > 6*n:
            return res
        
        while n_sum:
            # greedy
            roll_val = min(6,n_sum-n+1)
            res.append(roll_val)
            n_sum -= roll_val
            n -=1
        return res