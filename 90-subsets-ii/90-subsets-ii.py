class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        # using dfs
        def dfs(i):
            # out of bound
            # reached a leaf of the decision tree
            if(i >= len(nums)):
                result.append(subset.copy())
                return
                    
            # apply dfs on the left sub tree
            # on the left side we include the current value into our subset
            subset.append(nums[i])
            # call on next input
            dfs(i+1)
            # apply dfs on the right sub tree
            # on the right side we don't include the current value in our subset
            
            # poping out the value that was added while calling the left tree
            subset.pop()
            # call on the next input
            dfs(i+1)
        dfs(0)
        # duplicate check
        return list(set(tuple(sorted(r)) for r in result))
                    
            