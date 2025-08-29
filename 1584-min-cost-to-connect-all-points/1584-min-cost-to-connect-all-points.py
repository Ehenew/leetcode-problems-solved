class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False
        elif self.rank[x] > self.rank[y]:
            self.parent[ry] = rx
        elif self.rank[rx] < self.rank[y]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                edge_cost = + abs(xj - xi) + abs(yj - yi) # manhattan dist
                edges.append((edge_cost, i, j))

        edges.sort()
        uf = UnionFind(n)

        cost = 0
        for c, u, v in edges:
            if uf.union(u, v):
                cost += c
        return cost
