class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        if k == 0:
            return nums
        if 2 * k + 1 > n:
            return ans

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            ans[i] = total // (2 * k + 1)

        return ans