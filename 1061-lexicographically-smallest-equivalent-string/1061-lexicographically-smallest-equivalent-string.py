class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i + ord('a')): chr(i + ord('a')) for i in range(26)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

        for a, b in zip(s1, s2):
            union(a, b)

        return ''.join(find(c) for c in baseStr)