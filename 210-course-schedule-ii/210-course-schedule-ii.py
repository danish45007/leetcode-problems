class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_preq_map = {i: [] for i in range(numCourses)}
        for course,prereq in prerequisites:
            course_preq_map[course].append(prereq)
        course_visited = set()
        curr_path_visited = set()
        res = []
        
        def dfs(course):
            # if course in current path
            if course in curr_path_visited:
                return False
            # if course already been marked proccessed
            if course in course_visited:
                return True
            curr_path_visited.add(course)
            for prereq in course_preq_map[course]:
                if not dfs(prereq):
                    return False
            course_preq_map[course] = []
            curr_path_visited.remove(course)
            course_visited.add(course)
            res.append(course)
            return True
        
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        h