class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)
        
        def helper(node):
            for v in graph[node]:
                if colors[v] == -1:
                    colors[v] = 1  - colors[node]
                    if not helper(v):
                        return False
                elif colors[v] == colors[node]:
                    return False
            return True
        
        
        for node in range(len(graph)):
            if colors[node] == -1:
                colors[node] = 0
                if not helper(node):
                    return False
 
        return True
