class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash_map= {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hash_map[crs].append(pre)
        curr_cycle = set()
        visited = set()
        res = []
        def dfs(crs):
            if crs in curr_cycle:
                return False
            if crs in visited:
                return True
            curr_cycle.add(crs)
            for pre in hash_map[crs]:
                if dfs(pre) == False:
                    return False
            visited.add(crs)
            curr_cycle.remove(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
            