class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        return self.solve(nums,[],result)
    def solve(self,i,o,res):
        if len(i) == 0:
            if sorted(o) not in res:
                res.append(sorted(o))
            return
        o1 = o.copy()
        o2 = o.copy()
        o2.append(i[0])
        i = i[1:]
        self.solve(i,o1,res)
        self.solve(i,o2,res)
        return res
        
        