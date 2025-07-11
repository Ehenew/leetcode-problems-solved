from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1        
        min_heap = []

        for num, count in freq.items():
            heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heappop(min_heap)

        res = []
        for count, num in min_heap:
            res.append(num)

        return res

        