class Solution:
    def numTrees(self, n: int) -> int:
        number_of_trees = [1]*(n+1) #[nodes [0,n]]
        number_of_trees[0] = 1
        number_of_trees[1] = 1
        # starting from node 2 to n+1
        for node in range(2,n+1):
            total_trees = 0
            # for each node iterate over from 1 node+1 where in each itertion act as root
            for root in range(1,node+1):
                left_count = root - 1
                right_count = node - root
                total_trees += number_of_trees[left_count] * number_of_trees[right_count]
            
            number_of_trees[node] = total_trees
        return number_of_trees[n]