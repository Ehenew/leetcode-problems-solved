from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        left = 0
        freq = defaultdict(int)
        count_pairs = 0
        res = 0

        for right in range(len(nums)):
            count_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while count_pairs >= k:
                res += len(nums) - right
                freq[nums[left]] -= 1
                count_pairs -= freq[nums[left]]
                left += 1

        return res
