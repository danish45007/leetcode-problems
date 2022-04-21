class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i,comb,total):
            if total == target:
                res.append(comb.copy())
            if total > target or i > len(candidates):
                return
            prev = -1
            for i in range(i,len(candidates)):
                if candidates[i] == prev :
                    continue
                prev = candidates[i]
                
                comb.append(candidates[i])
                backtrack(i+1,comb,total+candidates[i])
                comb.pop()
            
        backtrack(0,[],0)
        return res
            
            
            
                