from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited.add(src)
            for neighbor, val in graph[src].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, dst, visited)
                if res != -1.0:
                    return val * res
            return -1.0

        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        
        return results
