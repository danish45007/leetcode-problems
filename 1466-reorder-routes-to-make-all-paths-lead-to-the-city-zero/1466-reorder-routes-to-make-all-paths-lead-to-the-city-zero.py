class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        changes = 0
        # set of valid edges
        valid_edges = {(a,b) for a,b in connections}
        # construct a city to neighbour adjacency list
        city_neighbour = {i:[] for i in range(n)}
        # populate valid_edges data into the adjacency list
        for a,b in valid_edges:
            city_neighbour[a].append(b)
            city_neighbour[b].append(a)
        # dfs to traverse
        def dfs(city):
            nonlocal visited, changes
            for n in city_neighbour[city]:
                if n in visited:
                    continue
                # not a valid edge
                if (n,city) not in valid_edges:
                    changes +=1
                visited.add(n)
                dfs(n)
        visited.add(0)
        dfs(0)
        return changes
                
                    
                

                 
        