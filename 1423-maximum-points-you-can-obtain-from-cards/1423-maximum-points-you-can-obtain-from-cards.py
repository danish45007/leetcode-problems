class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_card_sum = [0]*(k+1)
        right_card_sum = [0]*(k+1)
        max_score = 0
        _sum_so_far = 0
        for i in range(1,k+1):
            _sum_so_far += cardPoints[i-1]
            left_card_sum[i] = _sum_so_far
        _sum_so_far = 0
        for i in range(1,k+1):
            _sum_so_far += cardPoints[len(cardPoints) - i]
            right_card_sum[i] = _sum_so_far
        for i in range(len(right_card_sum)):
            max_score = max(max_score,left_card_sum[i]+right_card_sum[len(right_card_sum)-1-i])
        return max_score
            
            