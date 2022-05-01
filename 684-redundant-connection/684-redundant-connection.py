class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        def find_parent(node):
            parent = parents[node]
            # until don't reach at root parent
            while parent != parents[parent]:
                parent = parents[parent]
            return parent
        def union(node1,node2):
            parent1,parent2 = find_parent(node1),find_parent(node2)
            # redundant edge
            if parent1 == parent2:
                return False
            if rank[parent1] > rank[parent2]:
                # update parent 
                parents[parent2] = parent1
                # update rank
                rank[parent1] += 1
            else:
                # update parent 
                parents[parent1] = parent2
                # update rank
                rank[parent2] += 1
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]