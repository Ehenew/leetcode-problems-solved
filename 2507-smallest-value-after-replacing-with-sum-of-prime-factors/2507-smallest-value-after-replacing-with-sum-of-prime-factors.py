class Solution:
    def smallestValue(self, n: int) -> int:
        def sumPrimeFactors(x):
            tot = 0
            divisor = 2
            while divisor * divisor <= x:
                while x % divisor == 0:
                    tot += divisor
                    x //= divisor
                divisor += 1

            if x > 1:
                tot += x
            return tot
        
        while True:
            s = sumPrimeFactors(n)
            if s == n:
                return n
            n = s
