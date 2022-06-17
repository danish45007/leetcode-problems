class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        target = n
        candidates = [i for i in range(1,10)]
        def dfs(i,curr,total):
            # target case
            if total == target and len(set(curr)) == len(curr) == k:
                res.append(curr.copy())
                return
            # out of bound base
            if i >= len(candidates) or total > target:
                return
            # two choices 
            # include the current or don't include
            # choice 1
            curr.append(candidates[i])
            dfs(i,curr,total+candidates[i])
            # choice 2
            curr.pop()
            dfs(i+1,curr,total)
            
        dfs(0,[],0)
        return res