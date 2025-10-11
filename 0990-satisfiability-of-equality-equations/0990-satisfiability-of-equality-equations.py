class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i): chr(i) for i in range(97, 123)}  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[-1])

        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[-1]):
                    return False

        return True
