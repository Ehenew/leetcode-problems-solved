class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        
        if rx == ry:
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[ry] = rx
        elif self.rank[x] < self.rank[y]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v, w in roads:
            uf.union(u, v)
        
        r1 = uf.find(1)
        min_score = float('inf')
        for u, v, w in roads:
            if uf.find(u) == r1:
                min_score = min(min_score, w)

        return min_score
