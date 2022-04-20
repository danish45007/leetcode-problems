class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        # using dfs
        def dfs(i):
            # out of bound
            if i >= len(nums):
                # reached a leaf of the decision tree
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
        return result