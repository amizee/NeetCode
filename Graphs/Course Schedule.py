class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqsMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqsMap[course].append(prereq)
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            elif prereqsMap[course] == []:
                return True

            visit.add(course)
            for prereq in prereqsMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    
# Intuition: think of the prerequisites as a directed graph and create an adjacency list where a node's neighbours are their prerequisites.
# So if a cycle exists in the graph it is not possible to complete all the courses.
# Go through all edges in the graph and keep track of the current path to check for cycles, returning out immediately if there's a cycle.