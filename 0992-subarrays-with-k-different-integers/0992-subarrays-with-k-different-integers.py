class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(K):
            count = {}
            left = 0
            res = 0
            
            for right, val in enumerate(nums):
                count[val] = count.get(val, 0) + 1

                while len(count) > K:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                res += right - left + 1
            
            return res
        return atMost(k) - atMost(k - 1)