class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True


        factors = set()

        for i in range(2, n):
            if n % i == 0:
                factors.add(i)

        for factor in factors:
            if factor != 2 and factor != 3 and factor != 5:
                return False
                break
        return True