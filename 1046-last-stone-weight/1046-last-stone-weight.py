class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mx_heap = [-stone for stone in stones]

        heapify(mx_heap)

        while len(mx_heap) > 1:
            y = -1 * heappop(mx_heap)
            x = -1 * heappop(mx_heap)

            if x != y:
                y = y - x
                heappush(mx_heap, -y)

        return -1 * mx_heap[0] if len(mx_heap) > 0 else 0
            

