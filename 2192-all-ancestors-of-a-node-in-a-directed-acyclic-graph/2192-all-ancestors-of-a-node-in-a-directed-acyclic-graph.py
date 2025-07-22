from collections import defaultdict, deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        indegree = [0] * n


        for x, y in edges:
            graph[x].append(y)
            indegree[y] += 1

        
        ancest = [set() for _ in range(n)]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for neighbor in graph[node]:

                ancest[neighbor].add(node)

                indegree[neighbor] -= 1

                for an in ancest[node]:
                    ancest[neighbor].add(an)


                if indegree[neighbor] == 0:
                    q.append(neighbor)

        res = [sorted(list(s)) for s in ancest]

        return res

        

