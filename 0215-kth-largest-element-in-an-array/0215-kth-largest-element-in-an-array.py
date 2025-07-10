import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        my_bucket = []

        for num in nums:
            heapq.heappush(my_bucket, num)
            if len(my_bucket) > k:
                heapq.heappop(my_bucket)

        return my_bucket[0]