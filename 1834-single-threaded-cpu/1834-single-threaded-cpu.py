class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks_with_idx = [(i, enqT, proT) for i, (enqT, proT) in enumerate(tasks)]
        # idx, enquequeTime, processingTime
        res = []
        min_heap = []
        t = 0
        n = len(tasks)

        i = 0
        while len(res) < n:
            while i < n and tasks_with_idx[i][1] <= t:
                idx, enqT, proT = tasks_with_idx[i]
                heappush(min_heap, (proT, idx))
                i += 1

            if min_heap:
                proT, idx = heappop(min_heap)
                t += proT
                res.append(idx)

            else:
                t = tasks_with_idx[i][1]
            
        return res

          