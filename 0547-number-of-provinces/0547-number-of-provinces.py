class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n  

        def dfs(city):  
            if visited[city]:
                return
                                 
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1:
                    dfs(neighbor)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
        return provinces


