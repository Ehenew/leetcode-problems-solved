class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in range(k):
            heappush(heap, (nums1[0] + nums2[i], 0, i))

        while heap and len(res) < k:
            sum, i, j = heappop(heap)

            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))         

        return res






