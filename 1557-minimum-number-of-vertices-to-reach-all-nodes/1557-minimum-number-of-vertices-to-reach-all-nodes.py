class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree_counts = [0] * n

        for u, v in edges:
            indegree_counts[v] += 1
        ans = []
        for i in range(n):
            if indegree_counts[i] == 0:
                ans.append(i)

        return ans
            