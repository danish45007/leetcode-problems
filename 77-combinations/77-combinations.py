class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start,curr_combination):
            # base case
            if(len(curr_combination) == k):
                res.append(curr_combination.copy())
            for i in range(start,n+1):
                curr_combination.append(i)
                backtrack(i+1,curr_combination)
                curr_combination.pop()
        backtrack(1,[])
        return res