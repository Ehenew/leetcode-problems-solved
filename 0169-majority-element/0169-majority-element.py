from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_counts = Counter(nums)
        
        candidate = None

        for key in num_counts:
            if num_counts[key] > len(nums) / 2:
               candidate = key
        return candidate
        

        