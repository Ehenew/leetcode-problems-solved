class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        color = {i: 1 for i in range(numCourses)}

        def dfs(node):
            if color[node] == 2:
                return False  
            if color[node] == 3:
                return True   

            color[node] = 2 

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            color[node] = 3  
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
