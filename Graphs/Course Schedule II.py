class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqsMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqsMap[course].append(prereq)
        
        output = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for prereq in prereqsMap[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

# Intuition: similar approach where if you find a cycle you return out immediately.
# Since we need to maintain a valid order, a course is only added if all of its prerequisites can be completed. (output.append(course) and visit.add(course))
# We are running dfs() through all courses so visit needs to store all the courses that we have already checked otherwise it'll be duplicated in the output.