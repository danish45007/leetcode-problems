class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,curr,total):
            # target case
            if total == target:
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

        