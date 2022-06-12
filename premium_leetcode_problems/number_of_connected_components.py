'''
Problem
Given n, i.e. total number of nodes in an undirected graph numbered from 1 to n and an integer e, i.e. total number of edges in the graph. Calculate the total number of connected components in the graph. A connected component is a set of vertices in a graph that are linked to each other by paths.

Input Format:

First line of input line contains two integers n and e. Next e line will contain two integers u and v meaning that node u and node v are connected to each other in undirected fashion. 

Output Format:

For each input graph print an integer x denoting total number of connected components.

Constraints:

All the input values are well with in the integer range.

'''

def solve(edges,n):
    if n==1:
        return 1
    graph = {node: [] for node in range(n)}
    for node1,node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited = set()
    def dfs(node):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)
    res = 0
    for node in range(n):
        if node in visited:
            continue
        else:
            visited.add(node)
            res +=1
            dfs(node)
    return res                


if __name__ == "__main__":
    print(solve([[0,1],[1,2],[3,4]],5))