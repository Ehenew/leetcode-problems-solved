from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_count = defaultdict(int)
        mod_count[0] = 1   

        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod < 0:
                mod += k

            count += mod_count[mod]
            mod_count[mod] += 1

        return count
