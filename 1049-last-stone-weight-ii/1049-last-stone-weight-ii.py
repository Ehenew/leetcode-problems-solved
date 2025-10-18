class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_weight = sum(stones)
        half = total_weight // 2
        
        dp = [False] * (half + 1)
        dp[0] = True

        for s in stones:
            for j in range(half, s - 1, -1):
                dp[j] = dp[j] or dp[j - s]

        for j in range(half, -1, -1):
            if dp[j]:
                return total_weight - 2 * j
        