class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 0
        # comparing left neighors
        prev_child = ratings[0]
        left_to_right = [1]*len(ratings)
        for i in range(1,len(ratings)):
            curr_child = ratings[i]
            if curr_child > prev_child:
                left_to_right[i] = 1 + left_to_right[i-1]
            prev_child = curr_child
        
        # comparing right neighors
        prev_child = ratings[len(ratings)-1]
        right_to_left = [1]*len(ratings)
        for i in range(len(ratings)-2,-1,-1):
            curr_child = ratings[i]
            if curr_child > prev_child:
                right_to_left[i] = 1 + right_to_left[i+1]
            prev_child = curr_child
        
        for i in range(len(right_to_left)):
            res += max(left_to_right[i],right_to_left[i])
        return res
                