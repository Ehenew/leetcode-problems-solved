from functools import lru_cache
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        for u, v in richer:
            graph[v].append(u)
        
        @lru_cache(None)
        def dfs(person):
            quitest = person

            for richer in graph[person]:
                temp_quitest = dfs(richer)
                if quiet[temp_quitest] < quiet[quitest]:
                    quitest = temp_quitest

            return quitest


        ans = [i for i in range(n)]
        for i in range(n):
            ans[i] = dfs(i)

        return ans
        
# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         n = len(quiet)
#         graph = defaultdict(list)

#         for u, v in richer:
#             graph[v].append(u)

#         def dfs(person):
#             quitest = person

#             for richer in graph[person]:
#                 temp_quitest = dfs(richer)
#                 if quiet[temp_quitest] < quiet[quitest]:
#                     quitest = temp_quitest

#             return quitest


#         ans = [i for i in range(n)]
#         for i in range(n):
#             ans[i] = dfs(i)

#         return ans
        

        # # With BFS
        # n = len(quiet)
        # graph = defaultdict(list)
        # indegree = [0] * n
        
        # for a, b in richer:
        #     graph[a].append(b)
        #     indegree[b] += 1

        # q = deque()  
        
        # for i in range(n):
        #     if indegree[i] == 0:
        #         q.append(i)

        # ans = [i for i in range(n)]  
        # while q:
        #     person = q.popleft()
        #     for poorer in graph[person]:
        #         if quiet[ans[person]] < quiet[ans[poorer]]:
        #             ans[poorer] = ans[person]

        #         indegree[poorer] -= 1
        #         if indegree[poorer] == 0:
        #             q.append(poorer)

        # return ans
        

                

