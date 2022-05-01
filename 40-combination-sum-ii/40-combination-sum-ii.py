class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i,comb,total):
            if total==target:
                res.append(comb.copy())
                return
            
            if i>=len(candidates) or total>target:
                return
            
            comb.append(candidates[i])
            backtrack(i+1,comb,total+candidates[i])
            comb.pop()
            
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,comb,total)
        
        backtrack(0,[],0)
        return res
            
            
            
                