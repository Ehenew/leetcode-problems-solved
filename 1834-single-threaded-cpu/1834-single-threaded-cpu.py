class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks_with_idx = [(enqT, proT, i) for i, (enqT, proT) in enumerate(tasks)]
        # enquequeTime, processingTime, idx
        tasks_with_idx.sort()
        res = []
        min_heap = []
        t = 0

        i = 0
        while len(res) < len(tasks):
            while i < len(tasks) and tasks_with_idx[i][0] <= t:
                enqT, proT, idx = tasks_with_idx[i]
                heappush(min_heap, (proT, idx))
                i += 1

            if min_heap:
                proT, idx = heappop(min_heap)
                t += proT
                res.append(idx)

            elif len(min_heap) == 0:
                t = tasks_with_idx[i][0]
            
        return res

          