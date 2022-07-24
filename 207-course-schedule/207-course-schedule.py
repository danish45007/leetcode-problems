class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_preq_map = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            course_preq_map[course].append(prereq)
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for pre in course_preq_map[course]:
                if not dfs(pre):
                    return False
            course_preq_map[course] = []
            visited.remove(course)
            return True  
        
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # creating a hash_set to keep a mapping of course to its prerequisites
        hash_set = {i: [] for i in range(numCourses)}
        # populate the values to hash_set
        for course,prerequisite in prerequisites:
            hash_set[course].append(prerequisite)
        # creating a set to keep a record of all the visiting courses
        # courses will be added along dfs traversal
        visited = set()
        def dfs(course):
            # we are visiting the course the 2nd time
            if course in visited:
                return False
            # if the course doesn't have any prerequisites
            if hash_set[course] == []:
                return True
            # unique course visiting the first time
            visited.add(course)
            # iterating over prereq courses and calling dfs on them
            for pre in hash_set[course]:
                # fails for even one case return false
                if not dfs(pre): return False
            # processed for the current course so remove now
            visited.remove(course)
            # mark the pre-req as empty in hash set
            hash_set[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                
            