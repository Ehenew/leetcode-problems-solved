class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            if exp == 0:
                return 1
            half = power(base, exp // 2)
            half = (half * half) % MOD
            if exp % 2:
                half = (half * base) % MOD
            return half

        even_count = (n + 1) // 2
        odd_count = n // 2
        return (power(5, even_count) * power(4, odd_count)) % MOD
