class Solution:
    def numTrees(self, n: int) -> int:
        num_of_tree = [1] * (n+1)
        
        for node in range(2,n+1):
            total = 0
            for root in range(1,node+1):
                left_node = root - 1
                right_node = node - root
                total += num_of_tree[left_node]*num_of_tree[right_node]
                num_of_tree[node] = total
        return num_of_tree[n]