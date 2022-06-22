class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash_map= {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hash_map[crs].append(pre)
        curr_cycle = set() # course in current cycle (ongoing dfs)
        visited = set() # couse that has been visited
        res = []
        # def dfs(crs):
        #     if crs in curr_cycle:
        #         return False
        #     if crs in visited:
        #         return True
        #     curr_cycle.add(crs)
        #     for pre in hash_map[crs]:
        #         if dfs(pre) == False:
        #             return False
        #     visited.add(crs)
        #     curr_cycle.remove(crs)
        #     res.append(crs)
        #     return True
        # for c in range(numCourses):
        #     if dfs(c) == False:
        #         return []
        # return res
        res = []
        def dfs(course):
            if course in curr_cycle:
                return False
            if course in visited:
                return True
            curr_cycle.add(course)
            for prereq_course in hash_map[course]:
                if not dfs(prereq_course):
                    return False
            curr_cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
            