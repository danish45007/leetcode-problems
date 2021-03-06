class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
            Time: O(E+V)
            Space: O(V)
        '''
        safe = {} #{node: is_safe}
        res = []
        n = len(graph)
        def dfs(node):
            if node in safe:
                return safe[node]
            
            # marking the node not safe before visting its neighbours
            # to avoid stuck in the endless loop
            safe[node] = False
            # checking all the neighbours for the curr node
            # if atleast one of the neighbour is not safe mark it False
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return safe[node]
            safe[node] = True
            return safe[node]
        
        for node in range(n):
            if dfs(node):
                res.append(node)
        return res