from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        ab_sum = defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                ab_sum[a + b] += 1
        
        count = 0
        
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in ab_sum:
                    count += ab_sum[target]
        
        return count