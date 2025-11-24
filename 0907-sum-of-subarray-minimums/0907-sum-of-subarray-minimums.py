class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []  
        ans = 0

        for i in range(n + 1):
            curr = arr[i] if i < n else -1
            while stack and (arr[stack[-1]] > curr):
                idx = stack.pop()
                left_index = stack[-1] if stack else -1
                left_count = idx - left_index
                right_count = i - idx
                ans = (ans + arr[idx] * left_count * right_count) % MOD

            stack.append(i)
        return ans