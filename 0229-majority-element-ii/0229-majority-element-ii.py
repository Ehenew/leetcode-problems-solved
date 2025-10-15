from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        ans = []
        for val, fr in freq.items():
            if fr > n / 3:
                ans.append(val)

        return ans