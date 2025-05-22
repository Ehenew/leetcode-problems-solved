class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()

        for num in nums1:
            if num in nums2 and num not in seen:
                seen.add(num)
        return list(seen)