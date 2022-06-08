'''
Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
'''


from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # emtpy graph is valid Tree edge case
        if not n:
            return True
        # condtructing an adjacency list
        # for each vertex(V) map all the adjacent edges(E)
        # as the graph is undirected hence both way mapping
        _map = defaultdict(list)
        for vertex,edge in edges:
            _map[vertex].append(edge)
            _map[edge].append(vertex)
        visited = set()
        def dfs(curr_node,prev_node):
            if curr_node in visited:
                return False
            visited.add(curr_node)
            for neighour_node in _map[curr_node]:
                # skip the iteration
                if neighour_node == prev_node:
                    continue
                if not dfs(neighour_node,curr_node):
                    return False
            return True
        return dfs(0,-1) and n == len(visited)


        