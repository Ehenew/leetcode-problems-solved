class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        prev = nums[-1]
        for i in range(n - 2, -1, -1):
            curr = nums[i]
            if curr < prev:
                prev = curr
            else:
                k = math.ceil(curr / prev)
                ops += k - 1
                prev = curr // k
        return ops
